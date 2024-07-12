from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0

    if 'admin' in request.path:
        return {}

    try:
        # For authenticated users, get the cart using the user object or a different field
        if request.user.is_authenticated:
            # Adjust this based on your actual Cart model fields
            cart_id = _cart_id(request)  # Assume _cart_id function returns the cart_id
            cart = Cart.objects.get(cart_id=cart_id)
        else:
            # For non-authenticated users, get the cart based on cart_id from cookie or session
            cart_id = _cart_id(request)
            if cart_id:
                cart = Cart.objects.get(cart_id=cart_id)
            else:
                cart = None

        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        else:
            cart_count = 0

    except Cart.DoesNotExist:
        cart_count = 0

    return {'cart_count': cart_count}
