from django.contrib import admin
from .models import *

@admin.register(CartSession)
class CartSessionAdmin(admin.ModelAdmin):
    list_display = ('user','craeted','modified')

@admin.register(ItemSession)
class ItemSessionAdmin(admin.ModelAdmin):
    list_display = ('cart','product','count')
