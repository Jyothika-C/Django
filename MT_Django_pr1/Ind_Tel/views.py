from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hyderabad(request) :
        places = ["Golkonda" , "Sanghi" , "Charminar" , "Chilkur" , "Ramoji Film City"]
        context = {"places" : places}
        return render(request, "hyderabad.html", context)

def Warangal(request) :
        response = "<h1> Welcome to Warangal</h1>"
        return HttpResponse(response)