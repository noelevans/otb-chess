from django.db import models


class Address(models.Model):
    formatted = models.TextField(max_length=256)
    latitude = model.FloatField()
    longitude = model.FloatField()


class Player(models.Model):
    name = models.TextField(max_length=256)
    email = models.EmailField()
    biography = models.TextField(max_length=1024)
    default_contact_info = models.TextField(max_length=1024)
    member_since = models.DateTimeField()
    rating_lichess = models.IntegerField()
    rating_chessdotcom = models.IntegerField()
    rating_fide = models.IntegerField()


class Game(models.Model):
    proposer = models.ForeignKey(Player)
    opponent = models.ForeignKey(Player)
    group_event = models.BooleanField()
    description = models.TextField(max_length=2048)
    location_description = models.TextField(max_length=512)
    location_coords = models.ForeignKey(Address)
    start_time = models.DateTimeField()
    with_set = models.BooleanField()
    proposer_attended = models.BooleanField(initial=True)
    opponent_attended = models.BooleanField(initial=True)


class Message(models.Model):
    sender = models.ForeignKey(Player)
    recipient = models.ForeignKey(Player)
    content = models.TextField(max_length=2048)
    sent_time = models.DateTimeField()
