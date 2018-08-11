from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    scores = {}
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': week})
        scores[week] = response.json()
        scores = scores[week]
        scoreboard = scores['scoreboard']
        print(scoreboard)
    context = {
        'response': response,
        'scores': scores,
        'scoreboard': scoreboard,
    }
    return render(request, 'fantasy_football_api/index.html', context)