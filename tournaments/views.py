from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View
from .forms import TournamentForm
from .models import Tournament

class CreateTournament(View):

    template_name = 'tournaments/create_tournament.html'

    def get(self, request):
        form = TournamentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.organizer = request.user
            tournament.save()
            return redirect('tournament_list')
        return render(request, self.template_name, {'form': form, 'title':'Create Tournament'})

class Tournament(View):

    template_name = 'tournaments/list_tournaments.html'

    def get(self, request):
        tournaments = Tournament.objects.all()
        title = 'Tournaments'  
        return render(request, self.template_name, {'tournaments': tournaments, 'title': title})

