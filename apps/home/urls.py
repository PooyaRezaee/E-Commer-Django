from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:category_slug>/", HomeView.as_view(), name="category"),
]
