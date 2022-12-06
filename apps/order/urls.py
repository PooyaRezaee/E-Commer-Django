from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('payment/',PaymentView.as_view(),name='payment'),
    path('payment/pay/',PayView.as_view(),name='pay'),
]
