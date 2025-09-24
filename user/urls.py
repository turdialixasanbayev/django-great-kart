from django.urls import path

from . import views


urlpatterns = [
    path('sign-up/', views.SignUP.as_view(), name='sign_up'),
    path('sign-in/', views.SignIN.as_view(), name='sign_in'),
    path('sign-out/', views.SignOUT.as_view(), name='sign_out'),
]
