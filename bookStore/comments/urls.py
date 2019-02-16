from django.urls import path, include
from comments import views

urlpatterns = [
    path('', views.details, name='book_Details'),
]