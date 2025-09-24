from django.utils import timezone

from store.models import Category, Product

def global_context(request):
    context = {}
    current_year = timezone.now().year
    categories = Category.objects.filter(is_active=True).order_by('-name')
    products_count = Product.objects.filter(is_active=True).count()
    context['categories'] = categories
    context['current_year'] = current_year
    context['products_count'] = products_count
    return context
