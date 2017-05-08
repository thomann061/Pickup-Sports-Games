from django.db import models

class Game(models.Model):
    gameName = models.CharField(max_length=255)
    gameType = models.CharField(max_length=255)
    gameLocation = models.CharField(max_length=255)
    gameDateTime = models.DateTimeField()

    # To string
    def __str__(self):
        return 'Game #' + str(self.id)