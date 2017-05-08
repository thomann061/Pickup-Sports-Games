from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), max_length=100)

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-box'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), max_length=100)
    passwordVerify = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-box'}), label="Re-enter Password", max_length=100)