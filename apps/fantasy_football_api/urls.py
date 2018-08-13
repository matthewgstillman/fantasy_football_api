from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^boxscore$', views.boxscore, name="boxscore"),
    url(r'^crime$', views.crime, name="crime"),
    url(r'^leaguesettings$', views.leaguesettings, name="leaguesettings"),
    url(r'^playerinfo$', views.playerinfo, name="playerinfo"),
    url(r'^schedule$', views.schedule, name="schedule"),
    url(r'^seasonstats$', views.seasonstats, name="seasonstats"),
    url(r'^teams$', views.teams, name="teams"),
]
