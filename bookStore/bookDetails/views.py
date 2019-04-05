# =====================================================================================================
# CODE AUTHOR: RAUL ESPINOSA
# The views for the books.
# =====================================================================================================

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Import the Form for adding products from the Cart package
from cart.forms import AddToCartForm
from .forms import ReviewForm
# Import the Author and Book models from this package's models.py file
from .models import Author, Book, Review
from users.models import Profile
from wishlist.models import List


# List all the books. Allows one to filter books by author name,
# which is why there's a parameter called author_slug

def book_list(request, author_slug=None):
    # We assume no author was specified at first
    author = None

    # Display all authors
    authors = Author.objects.all()

    # Display all books
    books = Book.objects.all()

    # If an author slug was passed in, filter books displayed
    # by author name
    if author_slug:
        author = get_object_or_404(Author, slug=author_slug)
        books = books.filter(book_author=author)

    # Return the HTML page
    return render(request, 'bookDetails/book/list.html', {'author': author,
                                                          'authors': authors,
                                                          'books': books})

# Display a single book at a time


def book_info(request, book_name, slug):
    # Attempt to retrieve the book requested based on the provided
    # name and slug
    book = get_object_or_404(Book, book_name=book_name, slug=slug)

    # The form for Adding a product To the Cart (Add To Cart = ATC)
    ATC_product_form = AddToCartForm()

    # WISHLIST CODE: Gets the lists that the user has.
    myLists = getLists(request)

    # If we retrieved the book successfully, get its author
    # so we can reference their attributes in the HTML page
    if book:
        author_name = book.book_author
        author = get_object_or_404(Author, author_name=author_name)

    return render(request, 'bookDetails/book/detail.html', {'book': book,
                                                            'author': author,
                                                            'ATC_book_form': ATC_product_form})


def add_review(request, book_name, slug):
    book = get_object_or_404(Book, book_name=book_name, slug=slug) #Obtain book info
    User = get_object_or_404(Profile, user=request.user)           #Obtain user info for comment

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            message     = form.cleaned_data['message']
            name        = request.POST.get('name_select')       #Get value of name_select from radio buttons
            rating      = request.POST.get('rating')            #Get rating from stars
            review      = form.save(commit=False)
            review.book = book                                  #Get book for which this review is being applied to
            if name == "Username":                              #Check what user selected from name_select radio buttons
                review.name = User.user
            elif name == "Nickname":
                review.name = User.nick_name
                if len(review.name) == 0:                       #If nickname is not filled, use username
                    review.name = User.user
            elif name == "Anonymous":
                review.name = "Anonymous"
            else:
                review.name = "Anonymous"
            review.rating = rating
            #print("Username Display: " + review.user)          #Testing what username and rating are
            print("Rating submitted: " + review.rating)
            review.save()                                       #Save form and then redirect back to book_info page for
                                                                #specific book
            return redirect('bookDetails:book_info', book_name=book.book_name, slug=book.slug)
    else:
        form = ReviewForm()
        return render(request, 'bookDetails/book/add_review.html', {'form':form})


# function to get lists for user currently on the page.
def getLists(request):
    return List.objects.filter(user=request.user.profile).distinct()
