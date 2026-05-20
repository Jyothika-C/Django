from django.contrib import admin
from django.urls import path,include
from app1 import views


urlpatterns=[

    path('dashboard/',views.dashboard,name='dashboard'),
]