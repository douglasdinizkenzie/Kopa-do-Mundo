from teams.views import TeamsView
from django.urls import path

urlpatterns = [
    path("teams/", TeamsView.as_view()),
]
