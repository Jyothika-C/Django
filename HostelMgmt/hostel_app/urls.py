from django.urls import path
from . import views

urlpatterns = [

    # Admin
    path('dashboard', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('rooms/', views.rooms, name='rooms'),
    path('allocation/', views.allocation, name='allocation'),
    path('fees/', views.fees, name='fees'),
    path('complaints/', views.complaints, name='complaints'),

    # Student login
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    path('profile/', views.profile, name='profile'),

    path('room/', views.room, name='room'),

    path('complaints-student/', views.complaints_student, name='complaints_student'),

    path('fees-student/', views.fees_student, name='fees_student'),

]