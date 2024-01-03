from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from club.models import Club
from club.serializers import ClubSerializer

class ClubViewSet(viewsets.ModelViewSet):
    """CRUD for club. only admin user"""
    # queryset = Club.objects.all()
    # serializer_class = ClubSerializer
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )





