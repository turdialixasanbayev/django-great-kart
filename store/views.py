from django.views import View
from django.shortcuts import render

from .models import Product


class HomePageView(View):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        cat = request.GET.get('cat')
        products = self.get_queryset().order_by('?')

        if cat:
            products = products.filter(category__slug__iexact=cat)

        context = {'products': products}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        search = request.POST.get('q')
        products = self.get_queryset().order_by('?')

        if search:
            products = products.filter(name__icontains=search)

        context = {'products': products}

        return render(request, self.template_name, context)
