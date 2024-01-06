from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from club.models import Club
from club.serializers import ClubSerializer
from rest_framework.response import Response
from rest_framework.views import APIView





