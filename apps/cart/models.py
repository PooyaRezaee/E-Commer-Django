from django.db import models
from apps.home.models import Product
from apps.account.models import User

__all__  = [
    'CartSession',
    'ItemSession'
]
class ItemSession(models.Model):
    cart = models.ForeignKey('CartSession',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cart) + '-' + str(self.product)

class CartSession(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


    def total_price(self):
        prices = 0
        order_items = ItemSession.objects.filter(cart=self)
        for item in order_items:
            prices += item.product.price * item.count

        return prices

    def items(self):
        items = ItemSession.objects.filter(cart=self).order_by('craeted',)
        return items