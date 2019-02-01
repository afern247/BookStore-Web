# ====================================================================
# CODE AUTHOR: RAUL ESPINOSA
# This is the code for the actual cart functionality. A small note:
# I can't actually make the cart "work" until the models of the things
# that are supposed to go in the cart (i.e. the books) exist and can
# be imported/referenced. That being the case, I'm going to use some
# placeholder code to model the functionality needed. These can be
# refactored to the genuine book model code when it's available

# Note that I used the following resources to learn
# about django session functions and such:
# https://docs.djangoproject.com/en/2.0/topics/http/sessions/
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions
# ====================================================================

from django.conf import settings

# Importing Cart for the Cart class and Book
# for the Books (which I just wrote myself since the
# actual bookDetails haven't been made yet)
from cart.models import Book


# This data type simplifies floating-point arithmetic and makes it
# look more like what calculators make it look like in real life.
# Also allows for rounding rules to be established,
# which will help with price calculations

# Next we'd need to import the models class for the books, but that
# doesn't exist yet

# This is the cart class.


class Cart(object):
    # Constructor method for the class - includes a request parameter
    def __init__(self, request):
        # Start by creating a session for the new cart
        self.session = request.session
        try:
            # Get the userCart's session ID. If it fails, raises KeyError
            userCart = self.session.get(settings.CART_SESSION_ID)
        except:
            # If we can't, just make it a blank cart and handle KeyError
            userCart = self.session[settings.CART_SESSION_ID] = {}
        # Assign the newly created and ID'd userCart to this cart model
        self.userCart = userCart


    # Our cart's status has to be modifiable, i.e. we need to be able
    # to change the state of the cart dynamically. For this, we need
    # a save function
    def save(self):
        self.session.modified = True

    # This iterator will be used to iterate (of course) through the
    # books in the cart, i.e. the Book models (instances)

    def __iter__(self):
        # Get the keys corresponding to all the books
        # in the database
        book_names = self.userCart.keys()

        # Use the keys to get the actual Book objects
        # and add them to the cart
        books = Book.objects.filter(id__in=book_names)

        # Create a copy of the current cart
        cart = self.userCart.copy()

        # Add the books to the copy of the cart
        for book in books:
            cart[book.name]['book'] = book

        # Iterate over the books in the copied cart,
        # adding a price and total price attribute to each
        # item, then returning the book instance
        for book in cart.values():
            book['price'] = book.price
            book['total_price'] = book['price'] * book['amount']
            yield book

    # The function that will be used to add items to the cart.
    # Since no book models exist as of the present date (1/26/2019),
    # I have to start making assumptions here. I'll be using the Book Details
    # Feature Checklist as a guideline for what attributes the books will have and
    # name them accordingly

    # Of course, my app's Feature Checklist will be followed as well, hence
    # the change_amount parameter of the function ("Users can change the quantity
    # of items in the cart").
    def add(self, book, amount=1, change_amount=False):
        # The book's name, to be set to value of the corresponding
        # attribute of the book that was passed in as an argument
        # I'm assuming this will be a string - Django's JSON
        # serializes session data in string form ONLY
        book_name = book.name

        # If the book isn't in the cart, add it
        if book_name not in self.userCart:
            self.userCart[book_name] = {'amount': 0, 'price': book.price}

        # If change_amount is True, we change the number of the specified
        # book in the cart to the specified amount
        if change_amount:
            self.userCart[book_name]['amount'] = amount

        # Otherwise, we just add the specified amount of the specified book
        # to the cart
        else:
            self.userCart[book_name]['amount'] += amount

        # Save the state of the cart, cementing our changes
        self.save()

    # Now the function for removing books from the cart
    def remove(self, book):
        # Same idea as in the add() function - we use
        # the book's name as the key through which
        # we find the specified book in the cart, if it exists
        book_name = book.name

        # If the book is in the cart, remove it,
        # then save the state of the cart
        if book_name in self.userCart:
            del self.userCart[book_name]
            self.save()

