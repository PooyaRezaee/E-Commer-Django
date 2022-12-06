from apps.cart.utils import Cart

def order_fill(request):
    if request.user.is_authenticated:
        return {'order_fill': Cart(request.user.id).cart_exist}
    else:
        return{'order_fill': False}