from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PlayerReadOnlyViewSet




app_name = 'player'

router = DefaultRouter()

router.register(r'players', PlayerReadOnlyViewSet)

urlpatterns = [
    path('',include(router.urls))
]