from django.shortcuts import render, redirect
from django.contrib import messages # to display alert messages when the form data is valid
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'users/profile.html')