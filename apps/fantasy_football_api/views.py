from django.shortcuts import render, redirect
import requests
import espnff
from espnff import League

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

#Different API
# def league(request):
#     league_id = 446679
#     year = 2018
#     league = League(league_id, year)
#     team1 = league.teams[0]
#     print(league.teams)
#     print(league)
#     print(team1)
#     context = {
#         'league': league,
#         'team1': team1
#     }
#     return render(request, 'fantasy_football_api/league.html', context)


def playerinfo(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/playerInfo', 
                        params={'leagueId': 446679, 'playerId': 18311,'seasonId': 2018, 'matchupPeriodId': 1})
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
