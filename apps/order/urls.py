from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path("checkoout/", CheckoOutView.as_view(), name="checkout"),
    path("checkoout/add/<int:product_id>/", AddItemView.as_view(), name="add"),
    path("checkoout/subtract/<int:product_id>/", subtractItemView.as_view(), name="subtract"),
]
