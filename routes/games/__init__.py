from routes.games.games import Games
from flask_restful import Resource, request

class GameDescr(Resource):
    def get(self):
        return [
            {
                "name": "gameinfo",
                "url": "<id>/",
                "type": "public",
                "method": "GET",
                "descr": "Basic gameinfo."
            }
        ], 200

gameRoutes = [(GameDescr, '/'), (Games, '/<id>/')]