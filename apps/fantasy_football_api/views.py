from django.shortcuts import render, redirect
import json
import requests
import espnff
from espnff import League
import nflgame
import wikipedia
from .models import Player, Team
from player_id_dict import player_dict

# Create your views here.
def crime(request):
    url = ('http://nflarrest.com/api/v1/crime')
    response = requests.get(url)
    crime = response.json()
    print(crime)
    for i in crime:
        category = str(i['Category']).title()
        arrest_count = str(i['arrest_count'])
        print category, arrest_count
    context = {
        'crime': crime,
        'category': category,
        'arrest_count': arrest_count,
    }
    return render(request, 'fantasy_football_api/crime.html', context)

def index(request): 
    print("Player Dictionary: " + str(player_dict))
    scores = {}
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': week})
        scores[week] = response.json()
        scores = scores[week]
        scoreboard = scores['scoreboard']
        # logoUrl = scoreboard.matchups[0].teams[0].logoUrl
        # print("Logo URL: " + str(logoUrl))
        # print(scores)
        matchups = scoreboard['matchups']
        # print("Matchups" + str(matchups))
        team_array = []
        player_id_array = []
        #New Crazy Shit!
        if matchups:
            for matchup in matchups:
                teams = matchup['teams'] 
                # print("Teams: " + str(teams))
                # i = 0
                team = teams[0]['team']
                print("Team: " + str(team))
                team_array.append(team)
                players = teams[0]['playerIDs']
                print("Players: " + str(players))
                for player in players:
                    print("Player ID: "+ str(player))
                    player_id_array.append(player)
                    print("Player ID Array: " + str(player_id_array))
                    team_matchup = matchup['teams'][0]
                    print("Team Matchup: " + str(team_matchup))
                    team = matchup['teams'][0]['team']
                    print("Team: " + str(team))
                    team_array.append(team)
                    print("Player ID: " + str(player))
                    for week in range(1, 17):
                        response = requests.get('http://games.espn.com/ffl/api/v2/playerInfo', 
                                    params={'leagueId': 446679,                                                    'playerId': 60028,                                                     'seasonId': 2018,                                                      'matchupPeriodId': week})
                        players = response.json()
                        first_name = players['playerInfo']['players'][0]['player']['firstName']
                        last_name = players['playerInfo']['players'][0]['player']['lastName']
                        player_name = str(first_name) + " " + str(last_name)
                        print("Player Name: " + str(player_name))
                        # print ("Team: " + str(team))
                        # player_id = team
                        # print("Player ID: " + str(player_id))        
                        print("Player Dictionary: " + str(player_dict))
                        teams = player_dict['teams']
                        for team in teams:
                            print("Team: " + str(team))
                        context = {
                            'first_name': first_name,
                            'last_name': last_name,
                            'matchups': matchups,
                            'players': players,
                            'player_dict': player_dict,
                            'player_id_array': player_id_array, 
                            'response': response,
                            'scores': scores,
                            'scoreboard': scoreboard,
                            'team_array': team_array,
                            'teams': teams,
                            }
                        return render(request, 'fantasy_football_api/index.html', context)

def boxscore(request):
    scores = {}
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/boxscore', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': 1})
        scores = response.json()
        print("Scores: " + str(scores))
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
    mostarrests_list = []
    i = 0
    for i in mostarrests:
        mostarrests_list.append(i['Name'] + " " + str(i['Team']) + " " + str(i['Position'])+ " " + str(i['Team_city']) + " " + str(i['Team_name']) + " Arrest Count: " + str(i['arrest_count']))
        print (i['Name'] + " " + str(i['Team']) + " " + str(i['Position'])+ " " + str(i['Team_city']) + " " + str(i['Team_name']) + " Arrest Count: " + str(i['arrest_count']))
    # i = 0
    # for i in mostarrests[i]:
    #     print i
    context = {
        'mostarrests': mostarrests,
        'mostarrests_list': mostarrests_list,
    }
    return render(request, 'fantasy_football_api/mostarrests.html', context)


def playerinfo(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/playerInfo', 
                        params={'leagueId': 446679, 'playerId': 13982,'seasonId': 2018, 'matchupPeriodId': week})
        players = response.json()
        first_name = players['playerInfo']['players'][0]['player']['firstName']
        last_name = players['playerInfo']['players'][0]['player']['lastName']
        player_name = str(first_name) + " " + str(last_name)
        player_name_wiki = wikipedia.WikipediaPage(title=player_name)
        player_name_wiki_content = player_name_wiki.content
        player_name_wiki_images = player_name_wiki.images
        image_urls = player_name_wiki_images
    # print(first_image_url)
    context = {
        'player_name': player_name,
        'image_urls': image_urls,
        'players': players,
        'player_name': player_name,
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
    all_players = Player.objects.all()
    response = requests.get('http://api.fantasy.nfl.com/v1/players/stats?statType=seasonStats&season=2018&week=1&format=json')
    season_stats = response.json()
    print(season_stats)
    players = []
    for i in season_stats['players']:
        name = i['name']
        position = i['position']
        team = i['teamAbbr']
        projected_points = i['weekProjectedPts']
        week_pts = i['weekPts']
        season_pts = i['seasonPts']
        # Player.objects.add_player(name, position, team, projected_points, week_pts,season_pts)
        players.append(str(name) + " - " + str(position) + " - " + str(team) + " - Projected Weekly Points: " + str(projected_points) + " - Points Scored: " + str(week_pts) + " - Season Points: " + str(season_pts))
        print(str(name) + " - " + str(position) + " - " + str(team) + " - Projected Weekly Points: " + str(projected_points) + " - Points Scored: " + str(week_pts) + " - Season Points: " + str(season_pts))
        # print(players)
    context = {
        'all_players': all_players,
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


def scoring_leaders(request):
    scoring_leaders = []
    url = ('http://api.fantasy.nfl.com/players/scoringleaders?season=2018&week=1&format=json')
    response = requests.get(url)
    scoring_leaders = response.json()
    print("Scoring Leaders: " + str(scoring_leaders))
    positions = scoring_leaders['positions']
    wrs = positions['WR']
    for wr in wrs:
        player = wr['esbid']
        status = wr['status']
        stat_line = wr['statsLine']
        stats = wr['stats']
        team = wr['teamAbbr']
        opponent = wr['opponentTeamAbbr']
        first_name = wr['firstName']
        last_name = wr['lastName']
        full_name = str(first_name) + str(last_name)
        projected_points = wr['projectedPts']
        # stat_line = stat_line['stats']
        print("Stats: " + str(stats))
        # print("WR: " + str(wr))
    # print("Wide Receivers: " + str(wrs))
    context = {
        'player': player,
        'positions': positions,
        'scoring_leaders': scoring_leaders,
        'wrs': wrs,
    }
    return render(request, 'fantasy_football_api/scoring_leaders.html', context)


def team(request):
    response = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                    params={'leagueId': 446679, 'seasonId': 2018,'matchupPeriodId': 1})
    teams = response.json()
    scoreboard = teams['scoreboard']
    matchups = scoreboard['matchups']
    # player_ids = scoreboard['matchups'][0]['teams'][1]['playerIDs']
    context = {
        'matchups': matchups,
        'scoreboard': scoreboard,
    }
    return render(request, 'fantasy_football_api/team.html', context)


def teamcrime(request):
    url = ('http://nflarrest.com/api/v1/team/')
    response = requests.get(url)
    teamcrime = response.json()
    teamcrime_list = []
    print(teamcrime)
    for i in teamcrime:
        team_city = i['Team_city']
        team = i['Team_preffered_name']
        arrest_count = i['arrest_count']
        teamcrime_list.append(str(team) + " -  Arrest Count: " + str(arrest_count))
        print str(team) + " - " + str(arrest_count)
    context = {
        'teamcrime': teamcrime,
        'teamcrime_list': teamcrime_list,
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


def standings(request):
    for week in range(1, 17):
        response = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                        params={'leagueId': 446679, 'seasonId': 2018, 'matchupPeriodId': week})
        standings = response.json()
        # matchups = standings['scoreboard']['matchups']
        # print matchups
        # teams = matchups['teams']
        # print(teams)
        # print("Week " + str(week) + " " + str(response) + str(standings))
    context = {
        # 'matchups': matchups,
        'standings': standings,
    }
    return render(request, 'fantasy_football_api/standings.html', context)