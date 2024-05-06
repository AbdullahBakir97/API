from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('change-password/', views.PasswordChangeAPIView.as_view(), name='change_password'),
    path('password-reset/', views.PasswordResetAPIView.as_view(), name='password_reset'),
    path('password-reset-confirm/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
    
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    
    path('players/', views.PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='player-detail'),
    
    path('matches/', views.MatchList.as_view(), name='match-list'),
    path('matches/<int:pk>/', views.MatchDetail.as_view(), name='match-detail'),
    
    path('fantasy-teams/', views.FantasyTeamList.as_view(), name='fantasyteam-list'),
    path('fantasy-teams/<int:pk>/', views.FantasyTeamDetail.as_view(), name='fantasyteam-detail'),
    
    path('contests/', views.ContestList.as_view(), name='contest-list'),
    path('contests/<int:pk>/', views.ContestDetail.as_view(), name='contest-detail'),
    
    path('contest-entries/', views.ContestEntryList.as_view(), name='contestentry-list'),
    path('contest-entries/<int:pk>/', views.ContestEntryDetail.as_view(), name='contestentry-detail'),
]
