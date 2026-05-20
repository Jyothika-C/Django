
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def chittoor(request):
#     return render(request,"chittoor.html")
#     # response="<h1>welcome toChittoor</h1>"
#     # return HttpResponse(response)
def kadapa(request):
    response="<h1>welcome to kadapa</h1>"
    return HttpResponse(response)

def chittoor(request):
    user_name="Tony"
    age=45
    context={
    "name":user_name,
    "age":age
}
    # context={"name":user_name}
    response="<h1> Welcome to Chittoor</h1>"
    return render(request,"chittoor.html",context)