from django import forms
from .models import Tournament, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class TournamentForm(forms.ModelForm):
    
    class Meta:
        model = Tournament
        exclude = ['organizer', 'status', 'participants']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Remove help text for username
        self.fields['username'].help_text = ''
        # Remove help text for password1
        self.fields['password1'].help_text = ''
        # Remove help text for password2
        self.fields['password2'].help_text = ''

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'country', 'first_name', 'last_name']


# forms.py


