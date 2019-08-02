from django.contrib import admin
from django.urls import path, include
from projects import views

urlpatterns = [
    path('create/', views.createProject, name='create_project' ),
    path('view-project/', views.projects, name='project' ),
    path('s/', views.search, name='search'),
    path('<int:project_id>/assign_project/', views.assign_project, name='assign_project' ),
    path('<int:project_id>/submit_project/', views.submit_project, name='submit_project' ),
    path('<int:project_id>/confirm_project/', views.confirm_project, name='confirm_project' ),
    path('<int:project_id>/delete_project/', views.delete_project, name='delete_project' ),
    path('<int:project_id>/update_project/', views.update_project, name='update_project' ),
    path('issues/', views.issues, name='issues'),
    path('<int:project_id>/create_issue/', views.create_issue, name='create_issue' ),
    path('issue/<int:issue_id>/', views.issue, name='issue' ),
]