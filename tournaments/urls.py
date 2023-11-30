from django.urls import path
from .views import *

app_name = 'tournaments'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='tournaments/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('create_tournament/', CreateTournament.as_view(), name='create_tournament'),
    path('', list_Tournament.as_view(), name='list_tournaments'),    
    path('tournament/<int:id>', View_Tournament.as_view(), name='view_tournament'),    
    path('edit_tournament/<int:id>', EditTournament.as_view(), name='edit_tournament'),     
    path('no_permission/', NoPermission.as_view(), name='no_permission'),    
    path('delete_tournament/<int:id>', DeleteTournament.as_view(), name='delete_tournament'),      
    path('participating_tournament/', ParticipatingTournaments.as_view(), name='participating_tournament'),  
    path('index/', Index.as_view(), name='index'),     
]