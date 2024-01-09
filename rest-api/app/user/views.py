from django.shortcuts import render

from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from user.serializers import UserSerializer, AuthTokenSerializer

from user.models import User

from club.models import Club
from club.serializers import ClubSerializer

from match.models import Match
from match.serializers import MatchSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user

class UserFavoriteClubListView(generics.ListAPIView):
    serializer_class = ClubSerializer

    def get_queryset(self):
        user = self.request.user
        return user.favorite_teams.all()


class UserFavoriteMatchesView(generics.ListAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        user = self.request.user
        favorite_teams = user.favorite_teams.all()

        queryset = Match.objects.filter(home_team__in=favorite_teams) | Match.objects.filter(
            away_team__in=favorite_teams)

        return queryset