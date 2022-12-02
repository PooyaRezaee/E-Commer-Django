from apps.account.models import User
from apps.home.models import Product
from .models import *

class Cart:
    def __init__(self,user_id):
        self.user = User.objects.get(id=user_id)

    def order_exist(self):
        order = OrderDetail.objects.filter(user=self.user).exists()
        if order:
            self.order = OrderDetail.objects.get(user=self.user)
            return True
        else:
            return False

    def item_exist(self,order,product):
        if OrderItem.objects.filter(order=order,product=product).exists():
            return True
        else:
            return False
    
    def get_item(self,product_id):
        if not self.order_exist():
            payment = PaymentDetail.objects.create()
            self.order = OrderDetail.objects.create(user=self.user,payment=payment)
        else:
            self.order = OrderDetail.objects.get(user=self.user)

        product = Product.objects.get(id=product_id)
        if self.item_exist(self.order,product):
            item = OrderItem.objects.get(order=self.order,product=product)
        else:
            item = OrderItem.objects.create(order=self.order,product=product)
        
        return item
    

    def add_item(self,product_id):
        item = self.get_item(product_id)
        item.count += 1
        item.save()


    def delete_item(self,product_id):
        self.order = OrderDetail.objects.get(user=self.user)
        item = OrderItem.objects.get(order=self.order,product__id=product_id)
        item.delete()
        item_exist = OrderItem.objects.filter(order=self.order).exists()

        if not item_exist:
            self.order.delete()

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
        self.order = OrderDetail.objects.filter(user=self.user)
        if not self.order.exists():
            return False
        item = OrderItem.objects.filter(order=self.order.first(),product__id=product_id)
        if not item.exists():
            return False
        item = item.first()
        return item.count