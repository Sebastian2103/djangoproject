from rest_framework import serializers
from .models import Player
from club.serializers import ClubSerializer

class PlayerSerializer(serializers.ModelSerializer):
    club = ClubSerializer()  #serializator dla pola klub

    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'position',
            'age',
            'country',
            'club',
            'value',
        )

