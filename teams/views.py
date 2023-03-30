from rest_framework.views import status, Request, Response, APIView
from teams.models import Team
from django.forms.models import model_to_dict
from teams.utils import data_processing
from teams.exceptions import (
    NegativeTitlesError,
    ImpossibleTitlesError,
    InvalidYearCupError,
)


class TeamsView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        all_teams = [model_to_dict(for_teams) for for_teams in teams]
        return Response(all_teams, 200)

    def post(self, request):
        try:
            data_processing(request.data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"error": str(e)}, 400)
        new_team = Team.objects.create(**request.data)
        return Response(model_to_dict(new_team), 201)


class TeamsViewsDetails(APIView):
    def get(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        return Response(model_to_dict(team), 200)

    def patch(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team), 200)

    def delete(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team.delete()
        return Response(status=204)
