from django.http import HttpResponse
from django.shortcuts import render

tasks = ["foo", "bar", "Poo"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
