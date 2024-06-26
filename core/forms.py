from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Author: Jason Ngo, Maxine Ramos, Jenny Shen, Joyce Xuan
# Class: INF 453 - Capstone Project
# Supervisor: Maher Elshakankiri
# Purpose: creating forms for login and signup

## login form, with html styling
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6',
        'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6',
        'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
    }))

## signup form, with html styling
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6',
        'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full py-4 px-6',
        'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6',
        'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'w-full py-4 px-6',
        'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
    }))