from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tournament(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    players = models.ManyToManyField(User)


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    winner = models.ForeignKey(Team, related_name='won_matches', on_delete=models.CASCADE)


class Registration(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateTimeField()
