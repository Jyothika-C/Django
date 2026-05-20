from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def cart(request):
    return render(request,'cart.html')

def manage_menu(request):
    return render(request,'manage_menu.html')



