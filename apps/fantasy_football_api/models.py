from __future__ import unicode_literals

from django.db import models


class PlayerManager(models.Manager):
    def login(self, postData):
        return self

    def add_player(self, name, position, team, projected_points,week_pts, season_pts):
        self.create(name=name, position=position, team=team, projected_points=projected_points, week_pts=week_pts, season_pts=season_pts)
        return self

class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    projected_points = models.FloatField(max_length=100)
    week_pts = models.FloatField(max_length=200)
    season_pts = models.FloatField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlayerManager()

class TeamManager(models.Manager):
    def login(self, postData):
        return self

# Create your models here.
class Team(models.Model):
    team_location = models.CharField(max_length=50)
    team_nickname = models.CharField(max_length=50)
    wins = models.IntegerField()
    losses = models.IntegerField()
    division = models.CharField(max_length=50)
    score = models.FloatField(max_length = 1600)
    points_for = models.FloatField(max_length = 1600)
    points_against = models.FloatField(max_length = 1600)
    waiver_rank = models.IntegerField()
    overall_standing = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TeamManager()