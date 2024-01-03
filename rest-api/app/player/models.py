from django.db import models

from club.models import Club


# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    club = models.ForeignKey(Club, related_name='players', on_delete=models.CASCADE)
    value = models.CharField(max_length=60)

    def __str__(self):
        return self.name