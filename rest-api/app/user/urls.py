from django.urls import path

from . import views
from .views import UserFavoriteClubListView, UserFavoriteMatchesView

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
    path('favorite-club/', UserFavoriteClubListView.as_view(), name='favorite-club'),
    path('favorite-club-matches/', UserFavoriteMatchesView.as_view(), name='favorite-club'),
]