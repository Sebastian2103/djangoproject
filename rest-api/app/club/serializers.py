from rest_framework import serializers

from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = (
            'nation',
            'league',
            'full_name',
            'short_name',
            'stadium'
        )