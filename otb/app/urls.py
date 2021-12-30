from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    # path("app/", include("app.urls")),
    # path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path(
        "location/(?P<latitude>\d+\.\d+),(?P<longitude>\d+\.\d+)/distance/(?P<distance>\d+\.\d+)/",
        views.available_games,
    ),
]
