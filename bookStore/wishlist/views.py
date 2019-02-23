from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
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
Need to create a way that each page will link to each wishlist. wishlist/1 should be the wishlist
    for the user. Not just the id 1 for all the wishlists.
"""
def detail(request, wishlist_id):
    return HttpResponse("<h2>Details for Wishlist with ID: " + str(wishlist_id) + "</h2>")

"""
Need to do testing for the number of lists per user.
    May need to learn how to query for lists attached to a user
Need to do testing that only the list books shown per list per user is shown.
"""
@login_required()
def index(request):
    all_books = Book.objects.all()
    all_lists = List.objects.all()
    num_of_lists = List.objects.count()
    #num_of_lists = List.objects.count(List.user_name == Profile.user)

    return render(request, 'wishlist/index.html',
                  {'all_books': all_books, 'all_lists': all_lists, 'num_of_lists': num_of_lists})
