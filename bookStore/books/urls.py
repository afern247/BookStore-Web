from django.urls import path, include   # path is to create the path in urlpatterns
from . import views

urlpatterns = [
    path('', views.books, name='books-home'),
    path('details/', views.bookDetails, name='book-details'),
]
