from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    gameName = models.CharField(max_length=255)
    gameType = models.CharField(max_length=255)
    gameLocation = models.CharField(max_length=255)
    gameDateTime = models.DateTimeField()

    # To string
    def __str__(self):
        return 'Game #' + str(self.id)

class GameUser(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)

    # To string
    def __str__(self):
        return 'GameUser #' + str(self.id)