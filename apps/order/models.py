from django.db import models
from apps.home.models import Product
from apps.account.models import User

__all__ = [
    'OrderItem',
    'OrderDetail',
    'PaymentDetail',
]

class OrderItem(models.Model):
    order = models.ForeignKey('OrderDetail',on_delete=models.CASCADE,related_name='orders')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order) + '-' + str(self.product)

class OrderDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) +  '-' + str(self.user)

    def total(self):
        prices = 0
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            prices += item.product.price * item.count
        
        return prices
    
    def items(self):
        items = OrderItem.objects.filter(order=self).order_by('craeted',)
        return items
    
    def payment_stat(self):
        return PaymentDetail.objects.get(order=self).status

class PaymentDetail(models.Model):
    STATUS_CHOICES =(
        ("a", "Await"),
        ("p", "paid")
    )

    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='a')
    order = models.ForeignKey(OrderDetail,on_delete=models.CASCADE,related_name='payment')
    craeted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + '-' + str(self.order)