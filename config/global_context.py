from django.utils import timezone

from store.models import Category, Product

from checkout.models import Cart, CartItem

def global_context(request):
    context = {}
    current_year = timezone.now().year
    categories = Category.objects.filter(is_active=True).order_by('-name')
    products_count = Product.objects.filter(is_active=True).count()
    cart = Cart.objects.filter(user=request.user, is_active=True).first()
    items_count = CartItem.objects.filter(cart=cart, is_active=True).count()
    # items_count = cart.items_count
    context['categories'] = categories
    context['current_year'] = current_year
    context['products_count'] = products_count
    context['items_count'] = items_count
    return context
