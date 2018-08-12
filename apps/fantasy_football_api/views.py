from django.shortcuts import render, redirect
import json
import requests
import espnff
from espnff import League
import nflgame

# Create your views here.
def index(request):
    scores = {}
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': 1})
        scores[week] = response.json()
        scores = scores[week]
        scoreboard = scores['scoreboard']
        # logoUrl = scoreboard.matchups[0].teams[0].logoUrl
        # print(logoUrl)
        print(scores)
        # print(logoUrl)
    context = {
        'response': response,
        'scores': scores,
        'scoreboard': scoreboard,
    }
    return render(request, 'fantasy_football_api/index.html', context)

def boxscore(request):
    scores = {}
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/boxscore', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': 1})
        print(response.json())
        scores = response.json()
        # boxscores = boxscores[week]
        # scoreboard = scores['scoreboard']
        # print(scores)
    context = {
        'response': response,
        'scores': scores,
        # 'scoreboard': scoreboard,
    }
    return render(request, 'fantasy_football_api/boxscore.html', context)

def leaguesettings(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/leagueSettings', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': week})
        league_settings = response.json()
        print("League Settings: " + str(league_settings))
    context = {
        'league_settings': league_settings,
    }
    return render(request, 'fantasy_football_api/leaguesettings.html', context)


def playerinfo(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/playerInfo', 
                        params={'leagueId': 446679, 'playerId': 18311,'seasonId': 2018, 'matchupPeriodId': week})
        print(response.json())
        players = response.json()
        # scores = scores[week]
        # scoreboard = scores['scoreboard']
        # logoUrl = scoreboard.matchups[0].teams[0].logoUrl
        # print(logoUrl)
        # print(scores)
        # print(logoUrl)
    context = {
        'players': players,
    }
    return render(request, 'fantasy_football_api/playerinfo.html', context)


def schedule(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/schedule', 
                        params={'leagueId': 446679, 'seasonId': 2018})
        print(response.json())
        schedule = response.json()
    context = {
        'schedule': schedule,
    }
    return render(request, 'fantasy_football_api/schedule.html', context)


def seasonstats(request):
    response = requests.get('http://api.fantasy.nfl.com/v1/players/stats?statType=seasonStats&season=2017&week=1&format=json')
    season_stats = response.json()
    print(season_stats)
    context = {
        'season_stats': season_stats,
    }
    return render(request, 'fantasy_football_api/seasonstats.html', context)


def teams(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/teams', 
                        params={'leagueId': 446679, 'seasonId': 2018})
        print(response.json())
        teams = response.json()
        print("Teams: " + str(teams))
    context = {
        'teams': teams,
    }
    return render(request, 'fantasy_football_api/teams.html', context)


