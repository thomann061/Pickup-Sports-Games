from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "index.html"

# Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

# Login Function
def login_view(request):
    if request.user.is_authenticated():
        return render(request, 'logout.html')
    else:
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoginForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    # Store session data
                    request.session['username'] = form.cleaned_data['username']
                    return HttpResponseRedirect('/app')
                else:
                    # Add error message
                    messages.add_message(request, messages.ERROR, 'Try again.')
                    return HttpResponseRedirect('/login')     
        # if a GET (or any other method) we'll create a blank form
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

# Sign up View
def signup_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['passwordVerify']
            if password1 != password2:
                # Add error message
                messages.add_message(request, messages.ERROR, 'Your passwords don''t match.')
                return HttpResponseRedirect('/signup')
            # check if user exists
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                # Add error message
                messages.add_message(request, messages.ERROR, 'User already exists.')
                return HttpResponseRedirect('/signup')
            # Register user and login
            else:
                user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, user)
                # Store session data
                request.session['username'] = form.cleaned_data['username']
                return HttpResponseRedirect('/app')   
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

# Main App
def app_view(request):
    if request.user.is_authenticated():
        return render(request, 'app.html')
    else:
        return HttpResponseRedirect('/login')