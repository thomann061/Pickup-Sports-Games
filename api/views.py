from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Game
from django.contrib.auth.models import User
from .serializers import GameSerializer
from .permissions import IsAdminOrReadOnly
 
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly, )

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly, )