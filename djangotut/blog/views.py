from django.shortcuts import render
from django.http import HttpResponse

from .models import post

# Create your views here.

def home(request):
    return render(request, "home.html")

def add(request):
    post1 = post()
    post1.author = "mmmm"
    post1.title = "mmmmmmmmmmmmmm"
    post1.content = 'mmmmmmmmmmmm'
    return render(request , 'result.html' , {"post1" : post1})