from flask_restful import Resource
from utils.db import getConnection
from utils.utils import postJson 
from models.game import GameModel

class Games(Resource):
    def get(self, id):
        if(id == "all"):
            return {"games": GameModel.getAllDict()}
        else:
            game = GameModel.getById(id)
            if game is None:
                return {"kind": "GAME", "msg": "GameId out of scope."}, 403
            return {"game": {
                    "gameId":game.gameId,
                    "name": game.name,
                    "maxCaptains": game.maxCaptains,
                    "maxMembers": game.maxMembers,
                    "maxReservist": game.maxReservists
                }
            }, 200


class GamePage(Resource):
    def get(self, id):
        game = GameModel.getById(id)
        if game is None:
            return {"kind": "GAME", "msg": "GameId out of scope."}, 403
        return {"game_id": id, "page": game.getGamePage()}