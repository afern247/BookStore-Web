# =====================================================================================================
# CODE AUTHOR: RAUL ESPINOSA
# The views for the books.
# =====================================================================================================

from django.shortcuts import render, get_object_or_404

from .models import Author, Book


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

    return render(request, 'bookDetails/book/list.html', {'author': author,
                                                          'authors': authors,
                                                          'books': books})

# Display a single book at a time


def book_info(request, book_name, slug):
    # Attempt to retrieve the book requested based on the provided
    # name and slug
    book = get_object_or_404(Book, book_name=book_name, slug=slug)

    return render(request, 'bookDetails/book/detail.html', {'book': book})
