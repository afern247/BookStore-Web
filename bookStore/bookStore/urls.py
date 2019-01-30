from django.contrib import admin
from books import views as books_views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # User auth
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Navigation
    path('', include('storePage.urls')),        # Home page
    path('settings/', include('users.urls')),   # user profile, billing, etc. settings page
    path('wishlist/', include('wishlist.urls')), # Wishlist
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)