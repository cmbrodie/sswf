from django.shortcuts import render
from .models import Team

# Create your views here.


def youngest(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {"youngest_teams": list_teams}
    return render(request, "index.html", context)
