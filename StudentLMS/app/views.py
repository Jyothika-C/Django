from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import render


def student_list(request):

    students = Student.objects.all()

    return render(request, 'app/student_list.html', {
        'students': students
    })


def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'app/student_form.html', {
        'form': form
    })



def home(request):
    return render(request, 'app/home.html')