from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as do_logout, login as do_login


def login(request):
    """ login validation for the user """
    # Validation if user is authenticated
    if request.user.is_authenticated:
        return redirect('/')
    # Setting a form
    form = AuthenticationForm()
    # Validation data for the user
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Getting the user
            user = authenticate(username=username, password=password)
            # if user exists
            if user is not None:
                do_login(request, user)
                return redirect('/')
    # render for the login form
    return render(request, 'login.html', {'form': form})


def register(request):
    """ View to register a new user """
    # Validation if user is authenticated
    if request.user.is_authenticated:
        return redirect('/')
    # Setting a form
    form = UserCreationForm()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    # Validation data and creation of the new user
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/home')
    # render form to create user
    return render(request, 'register.html', {'form': form})


def logout(request):
    """ Logout for user """
    do_logout(request)
    return redirect('/login')
