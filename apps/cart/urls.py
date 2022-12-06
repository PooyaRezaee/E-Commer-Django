from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path("checkoout/", CheckoOutView.as_view(), name="checkout"),
    path("checkout/edit/", EditItemView.as_view(), name="edit"),
]
