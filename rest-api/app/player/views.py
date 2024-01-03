from rest_framework import viewsets, permissions
from player.models import Player
from player.serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated


class PlayerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

