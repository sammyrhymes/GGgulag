from django.urls import path
from .views import *

app_name = 'tournaments'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='tournaments/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('create_tournament/', CreateTournament.as_view(), name='create_tournament'),
    path('', list_Tournament.as_view(), name='list_tournaments'),    
]