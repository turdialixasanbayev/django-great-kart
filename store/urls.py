from django.urls import path

from .views import HomePageView, ProductDetailPageView, store_view


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
    path(
        'store-page/',
        store_view,
        name='store_page',
    ),
]
