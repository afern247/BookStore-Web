from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render (request, 'storePage/index.html')

def login(request):
    return HttpResponse("This is the login page")

def signup(request):
    return HttpResponse("This is the signup page")