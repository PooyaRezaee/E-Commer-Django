from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from .models import *
from .utils import Cart
import json

__all__ = [
    'CheckoOutView',
    'EditItemView'
]

class CheckoOutView(LoginRequiredMixin,View):
    def get(self,request):
        order = OrderDetail.objects.filter(user=request.user)
        if order.exists():
            order = order.get()
            return render(request,'order/checkout.html',{'orders':order.items,'order_detail':order})
        else:
            return render(request,'order/checkout.html')

class EditItemView(View):
    def post(self,request):
        data = json.load(request)
        type = data['type']
        product_id = data['product_id']

        cart = Cart(request.user.id)
        if type == "add":
            cart.add_item(product_id)
        elif type == "subtract":
            try:
                cart.subtract_item(product_id)
            except:
                return JsonResponse({'status':'n','message':'Item Not Exist'})

        
        return JsonResponse(
            {
                'status':'ok',
            }
            )