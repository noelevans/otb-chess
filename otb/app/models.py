from django.db import models


class Coord(models.Model):
    latitude = model.FloatField()
    longitude = model.FloatField()


class Player(models.Model):
    name
    games
    missed_games
    member_since = models.DateTimeField()


class Game(models.Model):
    proposer = models.ForeignKey(Player)
    description = models.TextField(max_length=2048)
    location_description = models.TextField(max_length=512)
    location_coords = models.ForeignKey(Coord)
    start_time = models.DateTimeField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
