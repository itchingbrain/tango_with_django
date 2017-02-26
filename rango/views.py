#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    msg = "Rango says hey there!"
    link = "<a href = /rango/about> About </a>"
    return HttpResponse(msg + " " + link)

def about(request):
    msg = "Here is the about page."
    back = "<a href = />back to main</a>"
    return HttpResponse(msg + "\n" + back)

