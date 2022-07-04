from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request, "firstapp/index.html")

def ab(request):
    return HttpResponse("Hello, Ab")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    name = name.capitalize()
    # or use name.capitalize() in the return statement, third arguement is called context
    return render(request, "firstapp/greet.html", {
        "name": name.capitalize()

    }) 


    