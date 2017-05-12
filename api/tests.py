from django.test import TestCase
from .models import Game
from datetime import date
from datetime import datetime
from django.test import Client

class GameTestCase(TestCase):

    def setUp(self):
        Game.objects.create(gameName="A Test", gameType="Basketball",
                            gameLocation="Jersey City, NJ", gameDateTime="2017-05-09T00:00:00Z")
        Game.objects.create(gameName="Test #2", gameType="Basketball",
                            gameLocation="Jersey City, NJ", gameDateTime="2017-05-09T00:00:00Z")
        self.theGame = Game.objects.get(id=1)

    def testAGamesName(self):
        self.assertEqual(self.theGame.gameName, "A Test")

    def testAGamesType(self):
        self.assertEqual(self.theGame.gameType, "Basketball")

    def testAGamesLocation(self):
        self.assertEqual(self.theGame.gameLocation, "Jersey City, NJ")

    def testAmountOfGames(self):
        count = Game.objects.count()
        self.assertEqual(count, 2)

    def testDeleteAGame(self):
        theGame = Game.objects.get(id=1)
        deletedGame = theGame.delete()
        self.assertEqual(deletedGame[0], 1)

    # Test REST Api
    def testRestGetAllGames200(self):
        c = Client()
        response = c.get('/api/games/')
        self.assertEqual(response.status_code, 200)

    def testRestGetSingleGames200(self):
        c = Client()
        response = c.get('/api/games/2/')
        self.assertEqual(response.status_code, 200)

    def testRestCreateSingleGame401(self):
        c = Client()
        response = c.post('/api/games/', { "gameName": "Test Name", "gameType": "Basketball", 
                                            "gameLocation": "Jersey", "gameDateTime": "2017-05-09T00:00:00Z" })
        self.assertEqual(response.status_code, 401)