from django.urls import path, include
from rest_framework.routers import SimpleRouter

from match.views import  CommentCreateView, CommentAdminViewSet,MatchAdminViewSet

app_name = 'match'

router = SimpleRouter()
router.register(r'admin', CommentAdminViewSet, basename='')
router1 = SimpleRouter()
router1.register(r'match', MatchAdminViewSet, basename='')
urlpatterns = [
path('comments/create/', CommentCreateView.as_view(), name='create_match_comment'),
path('comments/crud', include(router.urls)),
path('crud/', include(router1.urls))
]