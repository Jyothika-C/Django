from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
import json
from django.http import HttpResponse


# HOME

def home(request):

    return render(request, 'app/home.html')


# STUDENT LIST

def student_list(request):

    students = Student.objects.all()

    return render(request, 'app/student_list.html', {
        'students': students
    })


# ADD STUDENT

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


# UPDATE STUDENT

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    return render(request, 'app/update_student.html', {
        'form': form
    })


# DELETE STUDENT

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()

        return redirect('student_list')

    return render(request, 'app/delete_student.html', {
        'student': student
    })


# REPORTS

def reports(request):

    students = Student.objects.all()

    total_students = students.count()

    return render(request, 'app/reports.html', {
        'students': students,
        'total_students': total_students
    })


# BACKUP

def backup(request):

    students = list(Student.objects.values())

    for student in students:

        student['enroll_date'] = str(student['enroll_date'])

    data = json.dumps(students)

    response = HttpResponse(
        data,
        content_type='application/json'
    )

    response['Content-Disposition'] = 'attachment; filename="backup.json"'

    return response

# RESTORE

def restore(request):

    message = ""

    if request.method == 'POST':

        file = request.FILES['backup_file']

        data = json.load(file)

        for item in data:

            Student.objects.create(

                regno=item['regno'],
                name=item['name'],
                email=item['email'],
                program_level=item['program_level'],
                branch=item['branch'],
                year=item['year'],
                semester=item['semester'],
                enroll_date=item['enroll_date']

            )

        message = "Backup Restored Successfully"

    return render(request, 'app/restore.html', {
        'message': message
    })


# EXIT

def exit_page(request):

    return render(request, 'app/exit.html')