from django.db import models

# Create your models here.

class Club(models.Model):
    nation = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    stadium = models.CharField(max_length=255)

    def __str__(self):
        return self.short_name






