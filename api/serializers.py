from .models import Game, GameUser
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'id')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('gameOrganizer', 'gameType', 'gameVenue', 'gameAddress', 'gameCity', 'gameState', 'gameZip', 'gameDateTime', 'id')

class GameUserSerializer(serializers.ModelSerializer):
    game_info = GameSerializer(read_only=True, source='game')
    user_info = UserSerializer(read_only=True, source='user')

    class Meta:
        model = GameUser
        fields = ('game', 'user', 'id', 'game_info', 'user_info')