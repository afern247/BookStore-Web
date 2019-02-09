from django.shortcuts import render


# Books
def books(request):
    return render(request, 'books/books.html')

# Book details
def bookDetails(request):
    return render(request, 'books/bookDetails.html')


# =====================================================
# CODE AUTHOR: RAUL ESPINOSA
# Views necessary for the implementation of the add to cart functionality.
# =====================================================



# =====================================================
# RAUL'S CODE ENDS HERE
# =====================================================