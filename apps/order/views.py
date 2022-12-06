from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.cart.models import CartSession
from .utils import OrderManage
from django.contrib import messages
from apps.cart.models import CartSession

__all__ = [
    'PaymentView',
    'PayView'
]

class PaymentView(LoginRequiredMixin,View):
    def get(self,request):
        total_price = CartSession.objects.get(user=request.user.id).total_price
        return render(request,'order/payment.html',{'total_price':total_price})

class PayView(LoginRequiredMixin,View):
    def get(self,request):
        way = request.GET.get('way')
        match way:
            case 'paytest':
                order = OrderManage(request.user)
                cart = CartSession.objects.get(user=request.user)
                order_ = order.CreateOreder(cart.items)
                messages.success(request,'The order is pending payment',extra_tags='warning')
                order.OrderPaid(order_)
                messages.success(request,'The payment of the order was successfully completed',extra_tags='success')
                cart.delete()
                return redirect('home:index')