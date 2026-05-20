from django.shortcuts import render,redirect,get_object_or_404
from .models import StudentDetail
from .forms import StudentForm
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

# Create your views here.
def homepage(request):
    student_list=StudentDetail.objects.all()
    context={"students":student_list}
    return render(request,"homepage.html",context)
def addStudent(request):
    if request.method=="GET":
        form=StudentForm()
        context={
            "form":form
        }
        return render(request,"addStudent.html",context)
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    # return render(request,"addStudent.html")
    # form=StudentForm()
    # context={
    #     "form":form
    # }
    # return render(request,"addStudent.html",context)

# def details(request,id):
#     # given_id=f"selected id={id}"
#     # return HttpResponse(given_id)
#     student=get_object_or_404(StudentDetail,pk=id)
#     form=StudentForm(instance=student)
#     context={
#         "form":form
#     }
#     return render(request,"viewDetails.html",context)

def details(request, id):
    student = get_object_or_404(StudentDetail, pk=id)
    form = StudentForm(instance=student)
    context = {
        "form": form,
        "student": student
    }
    return render(request, "viewDetails.html", context)
def delete(request, id):
    student = get_object_or_404(StudentDetail, id=id)
    student.delete()
    return redirect('homepage')
def update(request, id):
    student = get_object_or_404(StudentDetail, pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            print("UPDATED SUCCESSFULLY")
            return redirect("homepage")
        else:
            print(form.errors)
    else:
        form = StudentForm(instance=student)
    context = {
        "form": form
    }
    return render(request, "update.html", context)

class StudentListCreateAPI(APIView):
    def get(self,request):
        students=StudentDetail.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class StudentRetriveUpdateDestoryAPI(APIView):
    def patch(self,request,pk):
        student=get_object_or_404(StudentDetail,pk=pk)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        student = get_object_or_404(StudentDetail, pk=pk)
        student.delete()
        return Response(
            {
                "message": "Student deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )