from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def students(request):
    return render(request, 'students.html')

def rooms(request):
    return render(request, 'rooms.html')

def allocation(request):
    return render(request, 'allocation.html')

def fees(request):
    return render(request, 'fees.html')

def complaints(request):
    return render(request, 'complaints.html')

#studentlogin
def student_dashboard(request):
    return render(request, 'studentlogin/student_dashboard.html')


def profile(request):
    return render(request, 'studentlogin/profile.html')


def room(request):
    return render(request, 'studentlogin/room.html')


def complaints_student(request):
    return render(request, 'studentlogin/complaints.html')


def fees_student(request):
    return render(request, 'studentlogin/fees.html')