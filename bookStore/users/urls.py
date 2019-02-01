from django.urls import path, include   # path is to create the path in urlpatterns
from . import views # Import the views defined in the current directory

urlpatterns = [
    path('', views.settingsHome, name='settings-home'),
    path('profile/', views.profile, name='profile-settings'),
    path('account/', views.accountSettings, name='account-settings'),
    path('billing/', views.billingSettings, name='billing-settings'),
    path('security/', views.securitySettings, name='security-settings'),
]

