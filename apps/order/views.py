from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

__all__ = [
    'PaymentView'
]

class PaymentView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'order/payment.html')

    def post(self,request):
        pass