from django.shortcuts import render, redirect
import json
import requests
import espnff
from espnff import League
import nflgame
import wikipedia

# Create your views here.
def crime(request):
    url = ('http://nflarrest.com/api/v1/crime')
    response = requests.get(url)
    crime = response.json()
    print(crime)

    # for crime in crime[0]:
    #     print(crime)
    # category = crime[0]
    # print("Category: " + str(category))
    # categories = []
    # for crime, i in crime:
    #     crime_category = crime[i]['Category']
    #     categories.append(crime_category)
    #     print(crime_category)
    #     i += 1
    context = {
        'crime': crime,
        # 'crime_category': crime_category,
    }
    return render(request, 'fantasy_football_api/crime.html', context)

def index(request):
    scores = {}
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': week})
        scores[week] = response.json()
        scores = scores[week]
        scoreboard = scores['scoreboard']
        # logoUrl = scoreboard.matchups[0].teams[0].logoUrl
        # print(logoUrl)
        print(scores)
        matchups = scoreboard['matchups']
        print("Matchups" + str(matchups))
        # for i in matchups:
            
        # i = 0
        # for i in matchups[i]:
        #     print (i[0])
        #     i += 1
    # i = 0
    # j = 0
    # for team in scoreboard['matchups'][0]['teams'][0]['team']['teamLocation']['title']:
    #     print (team)
    context = {
        'matchups': matchups,
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

def mostarrests(request):
    url = ('http://nflarrest.com/api/v1/player')
    response = requests.get(url)
    mostarrests = response.json()
    i = 0
    for i in mostarrests:
        print (i['Name'] +  str(i['Team']) + str(i['Position']) + str(i['Team_city']) + " Arrest Count: " + str(i['arrest_count']))
    # i = 0
    # for i in mostarrests[i]:
    #     print i
    context = {
        'mostarrests': mostarrests,
    }
    return render(request, 'fantasy_football_api/mostarrests.html', context)


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
    players = []
    for i in season_stats['players']:
        name = i['name']
        #Adding Photo Via Wikipedia Page
        # wiki_name = wikipedia.page(name + str("(American football)"))
        # print("Wiki Name: " + str(wiki_name) + str("(American football)"))
        position = i['position']
        team = i['teamAbbr']
        projected_points = i['weekProjectedPts']
        week_pts = i['weekPts']
        season_pts = i['seasonPts']
        players.append(str(name) + " - " + str(position) + " - " + str(team) + " - Projected Weekly Points: " + str(projected_points) + " - Points Scored: " + str(week_pts) + " - Season Points: " + str(season_pts))
        print(str(name) + " - " + str(position) + " - " + str(team) + " - Projected Weekly Points: " + str(projected_points) + " - Points Scored: " + str(week_pts) + " - Season Points: " + str(season_pts))
        # print(players)
    context = {
        'name': name,
        'players': players,
        'position': position,
        'projected_points': projected_points,
        'season_stats': season_stats,
        'season_pts': season_pts,
        'team': team,
        'week_pts': week_pts,
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


def teamcrime(request):
    url = ('http://nflarrest.com/api/v1/team/')
    response = requests.get(url)
    teamcrime = response.json()
    print(crime)

    # for crime in crime[0]:
    #     print(crime)
    # category = crime[0]
    # print("Category: " + str(category))
    # categories = []
    # for crime, i in crime:
    #     crime_category = crime[i]['Category']
    #     categories.append(crime_category)
    #     print(crime_category)
    #     i += 1
    context = {
        'teamcrime': teamcrime,
        # 'crime_category': crime_category,
    }
    return render(request, 'fantasy_football_api/teamcrime.html', context)

def teamarrests(request):
    base_url = ('http://nflarrest.com/api/v1/team/topPlayers/')
    # for i in teams:
    #     url = url + str(teams[i])
    #     print(url)
    first_response = requests.get(base_url)
    teamarrests = first_response.json()
    print(teamarrests)
    teams = ['ari', 'atl','bal','buf','car','chi', 'cin', 'cle','dal','den','det','gb','hou','ind','jax','kc','lac','lar','mia','min','ne','no','oak','phi','pit','sea','sf','tb','was']
    # print(teams)
    teamarrestsarray = []
    for team in teams:
        url = str(base_url) + str(team)
        print("URL: " + str(url))
        response = requests.get(url)
        team_url = response.json()
        #Logic I added that didn't work
        if team_url[0]['Name']:
            name = team_url[0]['Name']
            print(name)
            teamarrestsarray.extend(name)
        # print("Team URL: " + str(team_url))
    # print (teamarrestsarray)
    context = {
        'name': name,
        'team_url': team_url,
        'teams': teams,
        'teamarrestsarray': teamarrestsarray,
        'teamarrests': teamarrests,
    }
    return render(request, 'fantasy_football_api/teamarrests.html', context)