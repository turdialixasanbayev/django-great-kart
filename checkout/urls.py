from django.urls import path

from .views import CartPageView, AddToCartView, RemoveFromCartView, OrderPageView


cart_as_view = CartPageView.as_view()


urlpatterns = [
    path(
        'cart/',
        cart_as_view,
        name='cart',
    ),
    path(
        'order/',
        OrderPageView.as_view(),
        name='order',
    ),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
