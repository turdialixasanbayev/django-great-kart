from django.utils import timezone

from store.models import Category

def global_context(request):
    context = {}
    current_year = timezone.now().year
    categories = Category.objects.filter(is_active=True).order_by('-name')
    context['categories'] = categories
    context['current_year'] = current_year
    return context
