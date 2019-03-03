from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Address #, AddressInfo
from crispy_forms.helper import FormHelper

import re
from django.core.exceptions import ValidationError

# User registration form
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form to update username and email at the profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Form to upload new profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# Form to update first name and last name
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

# Form to upddate the user bio at the profile page
class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

    def __init__(self, *args, **kwargs):
        super(BioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class NicknameForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick_name']

    def __init__(self, *args, **kwargs):
        super(NicknameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address1', 'address2', 'city', 'state', 'zipcode']

    def __init__(self, *args, **kwargs):
        super(EditAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['name'].required = True
        self.fields['address1'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True
        self.fields['zipcode'].required = True

        self.fields['name'].widget.attrs[
            'placeholder'] = 'Shipping address familiar name'
        self.fields['address1'].widget.attrs['placeholder'] = 'Address 1'
        self.fields['address2'].widget.attrs['placeholder'] = 'Address 2'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zip Code'


class DeleteAddressForm(forms.Form):
    pass
