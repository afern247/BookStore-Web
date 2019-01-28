from django.shortcuts import render, redirect
from django.contrib import messages # to display alert messages when the form data is valid
from .forms import UserSignUpForm, UserUpdateForm, ProfileUpdateForm, UserProfileForm, BioAndSocialForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
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



@login_required
def profile(request):
    if request.method == 'POST':
        user_ProfileForm = UserProfileForm(request.POST, instance=request.user)
        user_BioAndSocialForm = BioAndSocialForm(request.POST, request.FILES, instance=request.user.profile)

        if user_ProfileForm.is_valid() and user_BioAndSocialForm.is_valid():
            user_ProfileForm.save()
            user_BioAndSocialForm.save()
            messages.success(request, f'Profile updated!')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        user_ProfileForm = UserProfileForm(instance=request.user)
        user_BioAndSocialForm = BioAndSocialForm(instance=request.user.profile)

    context = {
        'user_ProfileForm': user_ProfileForm,
        'user_BioAndSocialForm': user_BioAndSocialForm
    }

    return render(request, 'users/profile.html', context)


def settingsHome(request):
    return redirect('profile-settings')

def billingSettings(request):
    return render(request, 'users/billing.html')

def accountSettings(request):
    return render(request, 'users/account.html')

def securitySettings(request):
    return render(request, 'users/security.html')
