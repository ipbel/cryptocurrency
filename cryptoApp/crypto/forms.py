from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={
        'id': 'uname',
        'type': "text",
        'name': "username",
        'placeholder': "Username",
    }))

    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={
        'id': 'email',
        'type': "email",
        'name': "email",
        'placeholder': "Email",
    }))

    password1 = forms.CharField(required=True, label='Password', widget=forms.TextInput(attrs={
        'id': 'pass',
        'type': "password",
        'name': "password",
        'placeholder': "Password",
    }))

    password2 = forms.CharField(required=True, label='Password conformation', widget=forms.TextInput(attrs={
        'id': 'pass',
        'type': "password",
        'name': "password",
        'placeholder': "Confirm Password",
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

