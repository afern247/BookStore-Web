from django.shortcuts import render, redirect
from django.contrib import messages # to display alert messages when the form data is valid
from .forms import UserSignUpForm, UserUpdateForm, ProfileUpdateForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm



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


# the @ is a decorator, it adds functionality to the function
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)

        u_Passform = PasswordChangeForm(request.user, request.POST)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid() and u_Passform.is_valid() and user_form.is_valid():
            u_Passform.save()
            u_form.save()
            p_form.save()
            update_session_auth_hash(request, u_Passform)
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        u_Passform = PasswordChangeForm(request.user)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserForm(instance=request.user)
        # profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_Passform': u_Passform,
        'u_form': u_form,
        'p_form': p_form,
        'user_form': user_form
        # 'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)


def settingsHome(request):
    return redirect('profile-settings')

def billingSettings(request):
    return render(request, 'users/billing.html')

def accountSettings(request):
    return render(request, 'users/account.html')

def emailSettings(request):
    return HttpResponse('<h1>Email page</h1>')