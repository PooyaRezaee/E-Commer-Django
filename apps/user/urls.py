from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('address/',AddressesView.as_view(),name='addresses'),
    path('address/create/',CreateAddresView.as_view(),name='create-address'),
    path('address/delete/<pk>/',DeleteAddressView.as_view(),name='delete-address'),
    path('order/',OredersView.as_view(),name='orders'),
    path('order/<pk>/',OrederDetailView.as_view(),name='order'),
]
