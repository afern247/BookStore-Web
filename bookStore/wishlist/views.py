from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookDetails.models import Book
from .models import List
from users.models import Profile
from .forms import CreateList

allBooks = Book.objects.all()

#Function to get lists for user currently on the page.
def getLists(request):
    return List.objects.filter(user=request.user.profile).distinct()

def getBooksOfList(allMyLists, list):
    listValues = allMyLists.filter(name__contains=list.name).values('books')
    return Book.objects.filter(id__in=listValues)

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
    #Gets all the lists associated with the user and sets it to a variable.
    myLists = getLists(request)

    #Gets the count of all the lists associated with the user.
    myListsCount = myLists.count()

    #Values for if no lists exists.
    firstList = secondList = thirdList = []
    firstBooks = secondBooks = thirdBooks = []

    if myListsCount > 0:                #first list
        firstList = myLists[0]
        firstBooks = getBooksOfList(myLists, firstList)
        if myListsCount > 1:            #second list
            secondList = myLists[1]
            secondBooks = getBooksOfList(myLists, secondList)
            if myListsCount > 2:        #third list
                thirdList = myLists[2]
                thirdBooks = getBooksOfList(myLists, thirdList)

    return render(request, 'wishlist/index.html',
                  {'allBooks': allBooks, "myLists": myLists,
                   'myListsCount': myListsCount, 'firstList': firstList, 'firstBooks': firstBooks,
                   'secondList': secondList, 'secondBooks': secondBooks,
                   'thirdList': thirdList, 'thirdBooks': thirdBooks})
