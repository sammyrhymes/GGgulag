from django.urls import path
from .views import *

app_name = 'tournaments'

urlpatterns = [
    path('create_tournament/', CreateTournament.as_view(), name='create_tournament'),
    path('', Tournament.as_view(), name='list_tournament'),    
]