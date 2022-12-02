from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views import View
from .models import *
from apps.order.utils import Cart

__all__ = [
    'HomeView',
    'ProductDetailView',
]

class HomeView(ListView):
    template_name = 'home/index.html'
    context_object_name = 'products'
    ordering = ('created',)
    paginate_by = 24
    
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        products = Product.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            return products.filter(category=category)
        else:
            return products

class ProductDetailView(DetailView):
    template_name = 'home/detail.html'
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        count_item = Cart(self.request.user.id).count_item(context['object'].id)
        if count_item:
            context['count_item'] = count_item

        return context