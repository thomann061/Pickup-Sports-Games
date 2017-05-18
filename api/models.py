from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Game(models.Model):
    gameOrganizer = models.ForeignKey(User)
    gameType = models.CharField(max_length=50, default="Basketball")
    gameVenue = models.CharField(max_length=100, default="A Fake Park")
    gameAddress = models.CharField(max_length=100, default="Fake Address")
    gameCity = models.CharField(max_length=50, default="Jersey City")
    gameState = models.CharField(max_length=2, default="NJ")
    gameZip = models.CharField(max_length=20, default="07302")
    gameDateTime = models.DateTimeField()
    created_at = models.DateField(default=timezone.now)

    # To string
    def __str__(self):
        return 'Game #' + str(self.id)

class GameUser(models.Model):
    game = models.ForeignKey(Game, related_name="game_info")
    user = models.ForeignKey(User, related_name="user_info")
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('game', 'user')

    # To string
    def __str__(self):
        return 'GameUser #' + str(self.id)