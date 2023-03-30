from teams.views import TeamsView, TeamsViewsDetails
from django.urls import path

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<int:team_id>/", TeamsViewsDetails.as_view()),
]
