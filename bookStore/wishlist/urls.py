from django.urls import path
from . import views

app_name = 'wishlist'
urlpatterns = [
    path('<int:wishlist_id>', views.detail, name="detail"),
    path('', views.index, name='wishlist-home'),
]