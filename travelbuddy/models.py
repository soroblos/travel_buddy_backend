from django.db import models

class TravelBuddy(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    upvote = models.IntegerField()
    downvote = models.IntegerField()

