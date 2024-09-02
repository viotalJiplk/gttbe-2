from flask_restx import Resource
from utils import postJson, setAttributeFromList
from shared.models import GameModel
from datetime import datetime, date, time
from utils import jwsProtected
from shared.utils import perms
from utils import hasPermissionDecorator
from typing import List
from utils import AuthResult
from utils import errorList

accessibleAttributes = {
    "name": [str],
    "registrationStart": [date],
    "registrationEnd": [date],
    "maxTeams": [int],
}

class Games(Resource):
    @hasPermissionDecorator([perms.game.read, perms.game.listAll], True)
    def get(self, gameId, authResult: AuthResult, permissions: List[str]):
        """Gets game
        You can use <gameId> = all to list all games.

        Args:
            gameId (str): id of the game or 'all'

        Returns:
            dict: info about game or games
        """
        if(gameId == "all"):
            if perms.game.listAll in permissions:
                return {"games": GameModel.getAllDict()}
            else:
                raise errorList.permission.missingPermission
        else:
            if perms.game.read:
                game = GameModel.getById(gameId)
                if game is None:
                    raise errorList.data.doesNotExist
                return game.toDict(), 200
            else:
                raise errorList.permission.missingPermission

    @postJson
    @hasPermissionDecorator(perms.game.update, True)
    def put(self, gameId, data, authResult: AuthResult, permissions: List[str]):
        """Updates game

        Args:
            gameId (str): id of the game

        Returns:
            dict: info about game
        """
        game = GameModel.getById(gameId)
        setAttributeFromList(game, data, accessibleAttributes)
        return game.toDict()

class GamePage(Resource):
    @hasPermissionDecorator(perms.gamePage.read, True)
    def get(self, gameId, authResult: AuthResult, permissions: List[str]):
        """Gets gamepage

        Args:
            gameId (str): id of the game

        Returns:
            dict: gameid and gamepage
        """
        game = GameModel.getById(gameId)
        if game is None:
            raise errorList.data.doesNotExist
        gamePage = game.getGamePage()
        return {"game_id": gameId, "gamePage": gamePage}

    @postJson
    @hasPermissionDecorator(perms.gamePage.update, True)
    def put(self, data, authResult: AuthResult, permissions: List[str], gameId):
        """Updates gamepage

        Args:
            gameId (str): id of the game

        Returns:
            None:
        """
        game = GameModel.getById(gameId)
        if game is None:
            raise errorList.data.doesNotExist
        if "gamePage" in data and isinstance(data["gamePage"], str):
            game.gamePage = data["gamePage"]
        return
