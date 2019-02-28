from django.contrib import admin
from .models import Profile, Address#, AddressType

admin.site.register(Profile)
admin.site.register(Address)
# admin.site.register(AddressType)
