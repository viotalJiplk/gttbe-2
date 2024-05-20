from flask_restful import Resource
from utils.db import getConnection
from utils.utils import postJson
from utils.role import getRole
from models.game import GameModel
from datetime import date
from utils.jws import jwsProtected

class Games(Resource):
    def get(self, gameId):
        if(gameId == "all"):
            return {"games": GameModel.getAllDict()}
        else:
            game = GameModel.getById(gameId)
            if game is None:
                return {"kind": "GAME", "msg": "GameId out of scope."}, 403
            return game.toDict(), 200

    @jwsProtected()
    @postJson
    @getRole(["gameOrganizer", "admin"], optional=False)
    def put(self, data, authResult, hasRole, gameId):
        if gameId == 'all':
            if 'game_id' in data:
                gameId = data['game_id']
            else:
                return {"kind": "GAME", "msg": "GameId not specified."}, 403
        game = GameModel.getById(gameId)
        if game is None:
            return {"kind": "GAME", "msg": "GameId out of scope."}, 403
        if "registrationStart" in data and isinstance(data["registrationStart"], str):
            game.registrationStart = date.fromisoformat(data["registrationStart"])
        if "registrationEnd" in data and isinstance(data["registrationEnd"], str):
            game.registrationEnd = date.fromisoformat(data["registrationEnd"])
        if "maxCaptains" in data and isinstance(data["maxCaptains"], int):
            game.maxCaptains = data["maxCaptains"]
        if "maxMembers" in data and isinstance(data["maxMembers"], int):
            game.maxMembers = data["maxMembers"]
        if "maxReservists" in data and isinstance(data["maxReservists"], int):
            game.maxReservists = data["maxReservists"]
        if "minCaptains" in data and isinstance(data["minCaptains"], int):
            game.minCaptains = data["minCaptains"]
        if "minMembers" in data and isinstance(data["minMembers"], int):
            game.minMembers = data["minMembers"]
        if "minReservists" in data and isinstance(data["minReservists"], int):
            game.minReservists = data["minReservists"]
        if "maxTeams" in data and isinstance(data["maxTeams"], int):
            game.maxTeams = data["maxTeams"]
        game.update()
        return game.toDict()

class GamePage(Resource):
    def get(self, gameId):
        game = GameModel.getById(gameId)
        if game is None:
            return {"kind": "GAME", "msg": "GameId out of scope."}, 403
        return {"game_id": id, "page": game.getGamePage()}

    @jwsProtected()
    @postJson
    @getRole(["gameOrganizer"], optional=False)
    def put(self, data, authResult, hasRole, gameId):
        if gameId == 'all':
            if 'game_id' in data:
                gameId = data['game_id']
            else:
                return {"kind": "GAME", "msg": "GameId not specified."}, 403
        game = GameModel.getById(gameId)
        if game is None:
            return {"kind": "GAME", "msg": "GameId out of scope."}, 403
        if "gamePage" in data and isinstance(data["gamePage"], str):
            game.gamePage = data["gamePage"]
        game.update()
        return
    