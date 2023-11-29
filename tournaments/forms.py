from django import forms
from .models import Tournament
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TournamentForm(forms.ModelForm):
    
    class Meta:
        model = Tournament
        exclude = ['organizer', 'status']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
