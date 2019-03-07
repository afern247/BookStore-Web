from django.urls import path
from . import views

app_name = 'wishlist'
urlpatterns = [
    path('', views.index, name='wishlist-home'),
    path('create/', views.createList, name="createList"),
    path('delete/<int:list_id>', views.deleteList, name="deleteList"),
]