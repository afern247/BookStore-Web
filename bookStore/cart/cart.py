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

    # Next is the function that will be used to add items to the cart.
    # Since no book models exist as of the present date (1/26/2019),
    # I have to start making assumptions here. I'll be using the Book Details
    # Feature Checklist as a guideline for what attributes the books will have and
    # name them accordingly

    # Of course, my app's Feature Checklist will be followed as well, hence
    # the change_amount parameter of the function ("Users can change the quantity
    # of items in the cart")

    def add(self, book, amount=1, change_amount=False):
        # The book's name, to be set to value of the corresponding
        # attribute of the book that was passed in as an argument
        # I'm assuming this will be a string - Django's JSON
        # serializes session data in string form ONLY
        book_name = book.name

