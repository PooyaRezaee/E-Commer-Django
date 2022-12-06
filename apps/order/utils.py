from .models import *

class OrderManage:
    def __init__(self,user):
        self.user = user
            

    def _create_db(self):
        self.order = OrderDetail.objects.create(user=self.user,address=self.user.defualt_address)
        self.payment = PaymentDetail.objects.create(order=self.order)
    
    def _add_items(self,items):
        for item in items:
            OrderItem.objects.create(order=self.order,product=item.product,count=item.count)

    def CreateOreder(self,items):
        self._create_db()
        self._add_items(items)

        return self.order
    
    def OrderPaid(self,order):
        payment = PaymentDetail.objects.get(order=order)
        payment.status = "p"
        payment.save()

