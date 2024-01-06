from django.contrib import admin

from match.models import Match, Comment, PlayerRating

admin.site.register(Match)
admin.site.register(Comment)
admin.site.register(PlayerRating)

