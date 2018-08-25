from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
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
    objects = UserManager()