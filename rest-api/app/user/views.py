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

class UserFavoriteClubView(generics.CreateAPIView):
    serializer_class = ClubSerializer

    def perform_create(self, serializer):
        club_id = self.request.data.get('club_id')
        if club_id:
            try:
                club = Club.objects.get(pk=club_id)
                user = self.request.user
                user.favorite_teams.add(club)
                serializer.save(favorite_teams=user.favorite_teams.all())
            except Club.DoesNotExist:
                return Response({"error": "Club does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Club ID is required"}, status=status.HTTP_400_BAD_REQUEST)
