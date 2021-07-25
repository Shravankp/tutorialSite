from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>This is my first webapp</h1>')