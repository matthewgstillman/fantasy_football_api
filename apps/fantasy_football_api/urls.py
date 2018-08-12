from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^boxscore$', views.boxscore, name="boxscore"),
    # url(r'^league$', views.league, name="league"),
    url(r'^playerinfo$', views.playerinfo, name="playerinfo"),
]