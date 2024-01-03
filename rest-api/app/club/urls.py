from django.urls import path, include
from rest_framework.routers import DefaultRouter

from club import views

app_name = 'club'
router = DefaultRouter()

router.register('clubs', views.ClubViewSet, basename='clubs')

urlpatterns = [
    path('', include(router.urls))
]