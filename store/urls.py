from django.urls import path

from .views import HomePageView, ProductDetailPageView


urlpatterns = [
    path(
        '',
        HomePageView.as_view(),
        name='home',
    ),
    path(
        'product-detail/<slug:slug>/',
        ProductDetailPageView.as_view(),
        name='product_detail',
    ),
]
