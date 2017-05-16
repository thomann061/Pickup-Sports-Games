from .models import Game
from django.contrib.auth.models import User
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('gameType', 'gameVenue', 'gameAddress', 'gameCity', 'gameState', 'gameZip', 'gameDateTime', 'id')
