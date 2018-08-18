from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^boxscore$', views.boxscore, name="boxscore"),
    url(r'^crime$', views.crime, name="crime"),
    url(r'^leaguesettings$', views.leaguesettings, name="leaguesettings"),
    url(r'^mostarrests$', views.mostarrests, name="mostarrests"),
    url(r'^playerinfo$', views.playerinfo, name="playerinfo"),
    url(r'^schedule$', views.schedule, name="schedule"),
    url(r'^seasonstats$', views.seasonstats, name="seasonstats"),
    url(r'^teamarrests$', views.teamarrests, name="teamarrests"),
    url(r'^team$', views.team, name="team"),
    url(r'^teamcrime$', views.teamcrime, name="teamcrime"),
    url(r'^standings$', views.standings, name="standings"),
]
