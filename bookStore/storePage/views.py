from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'storePage/index.html')

def login(request):
    return HttpResponse("This is the login page")

def signup(request):
    return HttpResponse("This is the signup page")

