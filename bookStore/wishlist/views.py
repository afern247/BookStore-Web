from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookDetails.models import Book
from .models import List
from users.models import Profile
from .forms import CreateList

def create_list(request):
    form = CreateList(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('')
    return render(request, 'wishlist/index.html', {'form': form})

"""
Need to do testing for the number of lists per user.
    May need to learn how to query for lists attached to a user
Need to do testing that only the list books shown per list per user is shown.
"""
@login_required()
def index(request):
    #Gets all the lists associated with the user.
    myLists = List.objects.filter(books__list__user=request.user.profile).distinct()

    #Gets the count of all the lists associated with the user.
    listCount = myLists.count()

    all_books = Book.objects.all()

    #Need to put error checking for when no lists exists and for each amount of list.
    firstList = myLists[0]

    myListsValues = myLists.filter(name__contains=firstList.name).values('books')
    libros = Book.objects.filter(id__in=myListsValues)
    second = myLists[1]
    #secondBooks = Book.objects.filter(id__in=second.books)
    all_lists = List.objects.all()

    return render(request, 'wishlist/index.html',
                  {'all_books': all_books, 'all_lists': all_lists, "myLists": myLists,
                   'listCount': listCount, 'libros': libros, 'second': second,
                   #'secondBooks': secondBooks
                })
