from rest_framework import serializers

from user.serializers import UserSerializer
from match.models import Comment

from match.models import Match

from club.serializers import ClubSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'date_added', 'user_added', 'match')
        read_only_fields = ('date_added', 'user_added')

class MatchSerializer(serializers.ModelSerializer):
    home_team = ClubSerializer()  #serializer dla home_team
    away_team = ClubSerializer()  #serializer dla away_team
    class Meta:
        model = Match
        fields = ('id', 'date', 'location', 'home_team', 'away_team', 'result','stadium')
