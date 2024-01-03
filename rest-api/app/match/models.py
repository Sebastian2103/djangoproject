from django.db import models

from club.models import Club
from user.models import User
# Create your models here.
from player.models import Player
class Match(models.Model):
    """ Match model"""
    date = models.DateField()
    location = models.CharField(max_length=100)
    home_team = models.ForeignKey(Club, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, related_name='away_matches', on_delete=models.CASCADE)
    result = models.CharField(max_length=50)
    stadium = models.CharField(max_length=100)
    # players = models.ManyToManyField(Player, through='PlayerMatchStats', related_name='matches')


    def __str__(self):
        return (f"Data: {self.date} \n Miejsce: {self.location}\n"
                f" Home Team: {self.home_team} vs {self.away_team}\n"
                f" Result: {self.result}")



class Comment(models.Model):
    """Match comment model"""
    content = models.TextField()
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_added} - {self.match}"

# class PlayerMatchStats(models.Model):
#     "Model to store players raiting"
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     match = models.ForeignKey(Match, on_delete=models.CASCADE)
#     rating = models.DecimalField(max_digits=3, decimal_places=2)
#
#     def __str__(self):
#         return f"{self.player.name} - Match: {self.match.date} - Rating: {self.rating}"