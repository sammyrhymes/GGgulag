from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.http import urlencode
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import TournamentForm, LoginForm, SignupForm
from .models import Tournament

class LoginView(View):

    template_name = 'tournaments/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tournaments:list_tournaments')  
        return render(request, self.template_name, {'error': 'Invalid login credentials'})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('tournaments:login') 


class SignupView(View):
    template_name = 'tournaments/signup.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('tournaments:signup')

            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('tournaments:login')
        else:
            return redirect(request.path)


class CreateTournament(View):

    template_name = 'tournaments/create_tournaments.html'

    def get(self, request):
        if request.user.is_authenticated:    
            form = TournamentForm()
            return render(request, self.template_name, {'form': form})
        loginurl = reverse('tournaments:login') + '?' + urlencode({'next' : request.path})
        return redirect(loginurl)

    def post(self, request):
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.organizer = request.user
            tournament.save()
            return redirect('tournaments:list_tournaments')

class list_Tournament(View):

    template_name = 'tournaments/list_tournaments.html'

    def get(self, request):
        if request.user.is_authenticated:
            tournaments = Tournament.objects.values()
            title = 'Tournaments'  
            return render(request, self.template_name, {'tournaments': tournaments, 'title': title})
        loginurl = reverse('tournaments:login') + '?' + urlencode({'next' : request.path})
        return redirect(loginurl)

