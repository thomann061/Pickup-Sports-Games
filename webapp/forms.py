from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), max_length=100)

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), max_length=100)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), max_length=100)
    passwordVerify = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), label="Re-enter Password", max_length=100)

class GameForm(forms.Form):
    gameName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Name", max_length=100)
    gameType = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Type", max_length=100)
    gameLocation = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), label="Location", max_length=100)
    gameDateTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class' : 'form-control form-box'}), label="Date")