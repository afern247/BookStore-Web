from django.urls import path, include   # path is to create the path in urlpatterns
from . import views # Import the views defined in the current directory

# Name of the app needed for the namespace on urls.py
app_name = 'settings'

urlpatterns = [
    path('', views.settingsHome, name='settings-home'),
    path('profile/', views.profile, name='profile-settings'),
    path('account/', views.accountSettings, name='account-settings'),
    path('security/', views.securitySettings, name='security-settings'),
    path('billing/', views.billingSettings, name='billing-settings'),
    path('billing/<slug:address_slug>/', views.billingSettings, name='edit-address'),
]

