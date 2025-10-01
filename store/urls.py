from django.urls import path

from .views import HomePageView, ProductDetailPageView, store_view


urlpatterns = [
    path(
        '',
        HomePageView.as_view(),
        name='home',
    ),
    path(
        'store/',
        store_view,
        name='store',
    ),
    path(
        'detail/<slug:slug>/',
        ProductDetailPageView.as_view(),
        name='detail',
    ),
]
