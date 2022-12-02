from .models import Category
from apps.order.utils import Cart
def categories(request):
    return {'categories': Category.objects.all() }

def order_fill(request):
    return {'order_fill': Cart(request.user.id).order_exist}