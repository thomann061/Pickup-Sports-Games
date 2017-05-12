from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), max_length=50)

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), max_length=50)
    passwordVerify = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), label="Re-enter Password", max_length=50)

class GameForm(forms.Form):
    gameType = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Type", max_length=50)
    gameVenue = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Venue", max_length=50)
    gameAddress = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Address", max_length=50)
    gameCity = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="City", max_length=50)
    gameState = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="State", max_length=50)
    gameZip = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Zip", max_length=50)
    gameDateTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class' : 'form-control form-box'}), label="Date")