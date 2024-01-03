from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Comment, Match
from .serializers import CommentSerializer, MatchSerializer
# Create your views here.

class CommentCreateView(generics.CreateAPIView):
    """View for creating comments for a match"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        match_id = self.request.data.get('match')  # Pobranie identyfikatora meczu z danych żądania
        serializer.save(user_added=self.request.user, match_id=match_id)  # Zapis komentarza z odpowiednim meczem

class CommentAdminViewSet(viewsets.ModelViewSet):
    """Admin CRUD for comments"""
    queryset = Comment.objects.all()
    serializer_class = MatchSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )

class MatchAdminViewSet(viewsets.ModelViewSet):
    """Admin CRUD for match"""
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )