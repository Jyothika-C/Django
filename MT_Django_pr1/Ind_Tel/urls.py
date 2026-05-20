from django.urls import path
from Ind_Tel import views

urlpatterns = [
    path("hyderabad/", views.Hyderabad, name="Hyderabad"),
    path("warangal/", views.Warangal, name="Warangal")
]