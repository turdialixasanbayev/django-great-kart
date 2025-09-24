from django.views.generic import ListView

from .models import Product


class HomePageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)

        cat = self.request.GET.get('cat')

        if cat:
            queryset = queryset.filter(category__slug__exact=cat)

        return queryset.order_by('?')

    def post(self, request, *args, **kwargs):
        search = request.POST.get('q')
        """
        .
        """


"""
View da yozib koraman
"""
