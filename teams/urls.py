from django.urls import path, include
from teams import views

urlpatterns = [
    path('create_team/', views.create_team, name='create_team'),
    path('leaderboard/', views.leaderboard, name='leaderBoard'),
    path('manage_teams/', views.manage_teams, name='manage_teams'),
    path('teams/<int:team_id>/', views.team, name='team'),
    path('teams/<int:team_id>/delete_team/', views.delete_team, name='delete_team'),
    path('teams/<int:team_id>/update_team/', views.update_team, name='update_team'),
]