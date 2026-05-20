from django.contrib import admin
from django.urls import path
from Frontend import views

urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("cart/",views.cart, name="cart"),
    path("manage_menu/",views.manage_menu, name="manage_menu"),



]
