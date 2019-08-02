from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def leaderboard(request):
    teams = Team.objects.all().order_by('-total_points')
    length = len(teams)
    n = range(1, length+1)

    dictionary = {}
    position = []

    for x in n:
        position.append(x)

    for key,val in zip(position,teams):
        dictionary[key] = val

    print(dictionary)

    context = {
        'teams': teams, 'dictionary':dictionary,
    }
    return render(request, 'teams/leaderboard.html', context)

def create_team(request):
    users = User.objects.all()
    if request.POST:
        name = request.POST['name']
        members = request.POST.getlist('members')
        program_manager = request.POST.get('manager')

        program_manager = User.objects.get(username=program_manager)

        team = Team.objects.create(name=name, program_manager=program_manager)

        for member in members:
            user = User.objects.get(username=member)
            team.members.add(user)

        team.save()

        user = User.objects.get(username=program_manager)
        user.userprofile.is_program_manager = True
        user.save()
        
        messages.success(request, 'Team successfully created!')
        # return redirect("dashboard")

    context = {'users':users,}
    return render(request, 'teams/create-team.html', context)

def manage_teams(request):
    context ={

    }
    return render(request, 'accounts/manage-teams.html', context)

def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.POST:
        team.delete()
        messages.success(request, 'Team successfully deleted!')
        return redirect('dashboard')

    context = {
        'team': team,
    }
    return render(request, 'accounts/delete-team.html', context)

def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    context = {
        "team":team
    }
    return render(request, 'accounts/team.html', context)

def update_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    users = User.objects.all()

    if request.POST:
        for member in team.members.all():
            user = User.objects.get(username=member)
            team.members.remove(user)

        user = team.program_manager
        user.userprofile.is_program_manager = False
        user.save()
        
        team.name = request.POST['name']
        members = request.POST.getlist('members')
        program_manager = request.POST['manager']

        team.program_manager = User.objects.get(username=program_manager)

        for member in members:
            user = User.objects.get(username=member)
            team.members.add(user)

        team.save()

        user = User.objects.get(username=program_manager)
        user.userprofile.is_program_manager = True
        user.save()
        
        messages.success(request, 'Team successfully Updated!')
        return redirect('dashboard')

    context = {
        'team':team, 'users': users,
    }
    return render(request, 'accounts/update-team.html', context)