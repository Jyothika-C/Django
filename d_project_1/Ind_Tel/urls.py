from django.urls import path
from Ind_Tel import views

urlpatterns=[
    path("hyderabad/",views.hyderabad),
    path("warangal/",views.warangal),
]