from routes.games.games import Games, GamePage
from flask_restful import Resource, request

class GameDescr(Resource):
    def get(self):
        return [
            {
                "name": "gameinfo",
                "url": "<gameId>/",
                "type": "public",
                "method": "GET",
                "descr": "Basic gameinfo. You can use <gameId> = all to list all games."
            },
            {
                "name": "gamepage",
                "url": "<gameId>/page/",
                "type": "public",
                "method": "GET",
                "descr": "Game page in markdown."
            }
        ], 200

gameRoutes = [(GameDescr, '/'), (Games, '/<gameId>/'), (GamePage, '/<gameId>/page/')]
