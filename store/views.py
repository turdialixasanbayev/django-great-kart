from django.views import View
from django.shortcuts import render, get_object_or_404
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


class ProductDetailPageView(View):
    template_name = 'product-detail.html'

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug__iexact=slug, is_active=True)
        context = {'product': product}
        return render(request=request, template_name=self.template_name, context=context)


class StorePageView(View):
    template_name = 'store.html'
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(is_active=True).order_by('created_at')
        context = {}
        context['products'] = products[:8]
        return render(request, self.template_name, context)

store_view = StorePageView.as_view()
