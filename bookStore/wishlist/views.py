from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .models import List
from .forms import CreateList

def create_list(request):
    form = CreateList(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('')
    return render(request, 'wishlist/index.html', {'form': form})


@login_required()
def index(request):
    all_books = Book.objects.all()
    all_lists = List.objects.all()
    num_of_lists = List.objects.count()

    return render(request, 'wishlist/index.html',
                  {'all_books': all_books, 'all_lists': all_lists, 'num_of_lists': num_of_lists})
