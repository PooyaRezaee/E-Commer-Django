from django.db import models
from apps.home.models import Product
from apps.account.models import User

__all__  = [
    'CartSession',
    'ItemSession'
]

class CartSession(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class ItemSession(models.Model):
    cart = models.ForeignKey(CartSession,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cart) + '-' + str(self.product)