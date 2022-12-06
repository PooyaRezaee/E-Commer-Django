from apps.account.models import User
from apps.home.models import Product
from .models import *

class Cart:
    def __init__(self,user_id):
        self.user = User.objects.get(id=user_id)

    def cart_exist(self):
        cart = CartSession.objects.filter(user=self.user).exists()
        if cart:
            return True
        else:
            return False

    def item_exist(self,cart,product):
        if ItemSession.objects.filter(cart=cart,product=product).exists():
            return True
        else:
            return False
    
    def get_item(self,product_id):
        if not self.cart_exist():
            self.cart = CartSession.objects.create(user=self.user)
        else:
            self.cart = CartSession.objects.get(user=self.user)

        product = Product.objects.get(id=product_id)
        
        if self.item_exist(self.cart,product):
            item = ItemSession.objects.get(cart=self.cart,product=product)
        else:
            item = ItemSession.objects.create(cart=self.cart,product=product)
        
        return item
    

    def add_item(self,product_id):
        item = self.get_item(product_id)
        item.count += 1
        item.save()


    def delete_item(self,product_id):
        self.cart = CartSession.objects.get(user=self.user)
        item = ItemSession.objects.get(cart=self.cart,product__id=product_id)
        item.delete()
        item_exist = ItemSession.objects.filter(cart=self.cart).exists()

        if not item_exist:
            self.cart.delete()

    def subtract_item(self,product_id):
        item = self.get_item(product_id)
        if item.count == 1:
            self.delete_item(product_id)
            return None
        elif item.count <= 0:
            raise Exception('Item not exist')

        item.count -= 1
        item.save()

    def count_item(self,product_id):
        self.cart = CartSession.objects.filter(user=self.user)
        if not self.cart.exists():
            return False
        item = ItemSession.objects.filter(cart=self.cart.first(),product__id=product_id)
        if not item.exists():
            return False
        item = item.first()
        return item.count