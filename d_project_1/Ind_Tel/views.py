from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyderabad(request):
    places=["Golkonda","Sanghi","Charminar","Chilkur"]
    context={"places":places}
    return render(request,"hyderabad.html",context)
    # response="<h1>welcome to hyderabad</h1>"
    # return HttpResponse(response)
def warangal(request):
    response="<h1>welcome to warangal</h1>"
    return HttpResponse(response)
