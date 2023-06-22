from django.shortcuts import render
from django.http import HttpResponse
from .task import sleep_fun

def index(request):
    sleep_fun.delay(10)
    return HttpResponse("<h1>Hello, World!</h1>")