from .models import Game
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'gameName', 'gameType', 'gameLocation', 'gameDateTime')
