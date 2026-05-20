from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('student-list/', views.student_list, name='student_list'),

    path('add-student/', views.add_student, name='add_student'),

    path('update-student/<int:id>/', views.update_student, name='update_student'),

    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

    path('reports/', views.reports, name='reports'),

    path('backup/', views.backup, name='backup'),

    path('restore/', views.restore, name='restore'),

    path('exit/', views.exit_page, name='exit_page'),

]