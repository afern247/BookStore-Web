from django.shortcuts import render, redirect
from django.contrib import messages # to display alert messages when the form data is valid
from .forms import UserSignUpForm, ProfileUpdateForm, UserUpdateForm, UserProfileForm, BioForm, NicknameForm, AddressForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from users.models import Profile, Address


# User registration page
def signup(request):
    # If the request is a post, then proceed w/ the form
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        # To validate the form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }.')
            return redirect ('store-home-page')
    # if the request is not a post, then show a blank form
    else:
        # to use the form at signup we create an instance of the form we imported on top:
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})

# When the user clicks on the profile menu, he/she will be redirected here
def settingsHome(request):
    return redirect('profile-settings')

# Profile page
@login_required
def profile(request):
    if request.method == 'POST':
        user_ProfileForm = UserProfileForm(request.POST, instance=request.user)
        user_BioForm = BioForm(request.POST, instance=request.user.profile)
        user_NicknameForm = NicknameForm(request.POST, instance=request.user.profile)

        if user_ProfileForm.is_valid() and user_BioForm.is_valid() and user_NicknameForm.is_valid():
            user_ProfileForm.save()
            user_BioForm.save()
            user_NicknameForm.save()
            messages.success(request, f'Your profile has been updated successfully')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, f'There were some errors updating you profile.')

    else:
        user_ProfileForm = UserProfileForm(instance=request.user)
        user_BioForm = BioForm(instance=request.user.profile)
        user_NicknameForm = NicknameForm(instance=request.user.profile)


    context = {
        'user_ProfileForm': user_ProfileForm,
        'user_BioForm': user_BioForm,
        'user_NicknameForm': user_NicknameForm
    }

    return render(request, 'users/profile.html', context)


# Billing page (credit card and billing address)
def billingSettings(request):

    currentUser = request.user
    currentUser_userName = currentUser.username
    currentUserId = currentUser.id
    address_listNames = Address.objects.all().filter(user__user__username=currentUser_userName)

    # user_id = Address.objects.all().filter(user=currentUser.id)
    # for address in address_listNames:
    #     print (address.id)





    if request.method == 'POST':
        user_AddressForm = AddressForm(request.POST, instance=request.user.profile)

    else:
        user_AddressForm = AddressForm(instance=request.user.profile)
        # print(user_AddressForm)
        print(user_AddressForm)


    context = {
        'user_AddressForm': user_AddressForm
    }

    return render(request, 'users/billing.html', context)

# Username and email form
def accountSettings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, f'ERROR! Please read below')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/account.html', context)


# User password reset page
def securitySettings(request):
    if request.method == 'POST':
        u_Passform = PasswordChangeForm(request.user, request.POST)

        if u_Passform.is_valid():
            u_Passform.save()
            # update_session_auth_hash(request, u_Passform)
            update_session_auth_hash(request, u_Passform.user)
            messages.success(request, f'Password has been updated successfully')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, f'ERROR!')

    else:
        u_Passform = PasswordChangeForm(request.user)

    context = {
        'u_Passform': u_Passform
    }
    return render(request, 'users/security.html', context)
