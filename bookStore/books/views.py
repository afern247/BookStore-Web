from django.shortcuts import render, redirect
from django.contrib import messages                 # to display alert messages when the form data is valid

# Books
def books(request):
    return render(request, 'books/books.html')

# Book details
def bookDetails(request):
    return render(request, 'books/bookDetails.html')

