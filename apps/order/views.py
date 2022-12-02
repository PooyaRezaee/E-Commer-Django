from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .models import *
from .utils import Cart
__all__ = [
    'CheckoOutView',
    'AddItemView',
    'subtractItemView',
]

class CheckoOutView(LoginRequiredMixin,View):
    def get(self,request):
        order = OrderDetail.objects.filter(user=request.user)
        if order.exists():
            order = order.get()
            return render(request,'order/checkout.html',{'orders':order.items,'order_detail':order})
        else:
            return render(request,'order/checkout.html')

class AddItemView(View):
    def get(self,request,product_id):
        cart = Cart(request.user.id)
        cart.add_item(product_id)

        next = request.GET.get('next')
        if next == "checkout":
            return redirect('order:checkout')
        elif next == "detail":
            return redirect('home:detail',slug=request.GET.get('slug'))

class subtractItemView(View):
    def get(self,request,product_id):
        cart = Cart(request.user.id)
        
        try:
            cart.subtract_item(product_id)
        except:
            messages.warning(request,'Item Not Exist',extra_tags='warning')

        next = request.GET.get('next')
        if next == "checkout":
            return redirect('order:checkout')
        elif next == "detail":
            return redirect('home:detail',slug=request.GET.get('slug'))