from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm, GameForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from api.models import Game, GameUser
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
                    storeSessionData(request, user)
                    # Redirect to application
                    return HttpResponseRedirect('/map')
                else:
                    # Add error message
                    messages.add_message(request, messages.ERROR, 'Try again.')
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})   
        # if a GET (or any other method) we'll create a blank form
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

# Function to store session info
def storeSessionData(request, user):
    request.session['first_name'] = user.first_name

# Sign up View
def signup_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check if user exists
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                # Add error message
                messages.add_message(request, messages.ERROR, 'User already exists.')
                return render(request, 'signup.html', {'form': form})
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['passwordVerify']
            if password1 != password2:
                # Add error message
                messages.add_message(request, messages.ERROR, 'Your passwords don''t match.')
                return render(request, 'signup.html', {'form': form})
            # Register user and login
            else:
                user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'], 
                                                first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                                                email=form.cleaned_data['username'])
                login(request, user)
                # Store session data
                storeSessionData(request, user)
                return HttpResponseRedirect('/map')
        else:
            return render(request, 'signup.html', {'form': form})  
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

# Map View
def map_view(request):
    # Check if user is logged in
    if request.user.is_authenticated():
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            return HttpResponseRedirect('/map')
        # if a GET (or any other method) we'll create a blank form
        else:
            return render(request, 'map.html')
    # Redirect to login page if user is not logged in
    else:
        return HttpResponseRedirect('/login')

# Game View
def game_view(request):
    # Check if user is logged in
    if request.user.is_authenticated():
        gameUsers = GameUser.objects.filter(user=request.user)
        return render(request, 'games.html', {"games_list": gameUsers})
    # Redirect to login page if user is not logged in
    else:
        return HttpResponseRedirect('/login')

# New Game View
def new_game_view(request):
    # Check if user is logged in
    if request.user.is_authenticated():
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = GameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                game = Game.objects.create(gameType=form.cleaned_data['gameType'], gameVenue=form.cleaned_data['gameVenue'],
                                    gameAddress=form.cleaned_data['gameAddress'], gameCity=form.cleaned_data['gameCity'],
                                    gameState=form.cleaned_data['gameState'], gameZip=form.cleaned_data['gameZip'],
                                    gameDateTime=form.cleaned_data['gameDateTime'])
                GameUser.objects.create(game=game, user=request.user)
                return HttpResponseRedirect('/games')
            else:
                return render(request, 'new-game.html', {"form": form})
        else:
            form = GameForm()
            return render(request, 'new-game.html', {"form": form})
    # Redirect to login page if user is not logged in
    else:
        return HttpResponseRedirect('/login')

# Feed View
def feed_view(request):
    # Check if user is logged in
    if request.user.is_authenticated():
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            return HttpResponseRedirect('/feed')
        # if a GET (or any other method) we'll create a blank form
        else:
            # Get last 10 results
            gameUsers = GameUser.objects.all()[:10]
            return render(request, 'feed.html', {"games_list": gameUsers})
    # Redirect to login page if user is not logged in
    else:
        return HttpResponseRedirect('/login')

# Profile View
def profile_view(request):
    if request.user.is_authenticated():
        # Send request with user info
        return render(request, 'profile.html', {'user': request.user} )
    else:
        return HttpResponseRedirect('/login')