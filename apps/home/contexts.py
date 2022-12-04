from apps.order.utils import Cart

def order_fill(request):
    if request.user.is_authenticated:
        return {'order_fill': Cart(request.user.id).order_exist}
    else:
        return{'order_fill': False}