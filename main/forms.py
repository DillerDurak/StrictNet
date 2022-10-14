from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import *

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=16)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'type':"text",
        'name':"message", 
        'id':"form", 
        'placeholder':"Введите текст..."}), 
        max_length=1000)

