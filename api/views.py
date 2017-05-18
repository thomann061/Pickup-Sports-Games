from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Game, GameUser
from django.contrib.auth.models import User
from .serializers import GameSerializer, GameUserSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly, IsGameCreator, IsGameUserCreator, IsUserAndReadAndCreate
 
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly, )

class UserSignedInDetail(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        """
        This view should return a list of all the games
        for the currently authenticated user.
        """
        user = self.request.user
        return User.objects.filter(id=user.id)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsGameCreator, )

class SingleGamesListOfUsers(generics.ListCreateAPIView):
    serializer_class = GameUserSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        """
        This view should return a list of all the users
        of a game specified game.
        """
        gameId = self.kwargs['pk']
        gameusers = GameUser.objects.filter(game=gameId)
        return gameusers


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )

class GameUserList(generics.ListCreateAPIView):
    serializer_class = GameUserSerializer
    permission_classes = (IsUserAndReadAndCreate, )

    def get_queryset(self):
        """
        This view should return a list of all the games
        for the currently authenticated user.
        """
        user = self.request.user
        return GameUser.objects.filter(user=user)

class GameUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameUser.objects.all()
    serializer_class = GameUserSerializer
    permission_classes = (IsGameUserCreator, )

    # def delete(self, request, *args, **kwargs):
    #     if(request.user.id == self.get_object())
    #     # instance = self.get_object()
    #     # self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)