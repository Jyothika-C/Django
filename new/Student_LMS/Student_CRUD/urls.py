from django.contrib import admin
from django.urls import path
from Student_CRUD import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-student/', views.addStudent, name='addStudent'),
    path("details/<int:id>/",views.details,name="details"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path("api/students/",views.StudentListCreateAPI.as_view(),name="Student-list-create-API"),
    path("api/students/<int:pk>" , views.StudentRetriveUpdateDestoryAPI.as_view() ,name = "Student-retrive-update-destroy-API" )
]
