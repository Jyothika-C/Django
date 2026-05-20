from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def students(request):
    return render(request, 'student.html')