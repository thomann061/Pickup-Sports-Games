from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    gameType = models.CharField(max_length=50, default="Basketball")
    gameVenue = models.CharField(max_length=100, default="A Fake Park")
    gameAddress = models.CharField(max_length=100, default="Fake Address")
    gameCity = models.CharField(max_length=50, default="Jersey City")
    gameState = models.CharField(max_length=2, default="NJ")
    gameZip = models.CharField(max_length=20, default="07302")
    gameDateTime = models.DateTimeField()

    # To string
    def __str__(self):
        return 'Game #' + str(self.id)

class GameUser(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)
    isOrganizer = models.BooleanField(default=0)

    # To string
    def __str__(self):
        return 'GameUser #' + str(self.id)