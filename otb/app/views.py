import math


from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def euclidean_distance(latitude, longitude, game):
    x = abs(latitude - game.location_coords__latitude)
    y = abs(longitude - game.location_coords__longitude)
    return math.sqrt(x * x + y * y)


def available_games(latitude, longitude, distance):
    games = Game.objects.filter(
        (Q(oppenent=None) | Q(group_event=True)),
        acceptable_distance(lat, lng, distance),
        start_time__gt=datetime.datetime.now(),
    )
    context = {
        "games": [
            game
            for game in games
            if pythagorean_distance(latitude, longitude, game) < distance
        ]
    }
    return render(request, "app/available_games.html", context)
