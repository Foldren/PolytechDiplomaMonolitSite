from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('reg_shop', views.ActionRegistrationShop),
]

