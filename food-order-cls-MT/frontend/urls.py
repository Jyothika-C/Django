from django.urls import path
from frontend import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("cart/", views.cart, name="cart"),
    path("manage-menu/", views.manage_menu, name="manage-menu"),
]
