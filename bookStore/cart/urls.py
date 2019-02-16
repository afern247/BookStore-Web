# =====================================================
# CODE AUTHOR: RAUL ESPINOSA
# The URLs for the cart
# =====================================================

from django.urls import path

from . import views

# The name of the app being used; in this case
# it's the cart app
app_identifier = 'cart'

# The actual URL patterns
urlpatterns = [
    path('', views.cart_info, name='cart_info'),
    path('add/<str:book_name>/', views.addToCart, name='addToCart'),
    path('remove/<str:book_name>/', views.removeFromCart, name='removeFromCart')
]