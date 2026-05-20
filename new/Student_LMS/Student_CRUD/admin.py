from django.contrib import admin
from .models import StudentDetail
# Register your models here.

# admin.site.register(StudentDetail)

class StudentAdmin(admin.ModelAdmin):
    list_display=("student_name","email","course","enrollment_date")
    search_fields=("student_name","email","course")
    list_filter=("course",)  #("Course")

admin.site.register(StudentDetail,StudentAdmin)
