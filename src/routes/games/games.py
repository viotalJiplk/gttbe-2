from flask_restx import Resource
from utils import postJson, setAttributeFromList, AuthResult, errorList, jwsProtected, hasPermissionDecorator, returnParser, returnError, postJsonParse
from shared.models import GameModel
from datetime import datetime, date, time
from shared.utils import perms, DatabaseError
from typing import List
from copy import deepcopy
from helper import getGame

accessibleAttributes = {
    "name": [str],
    "registrationStart": [date],
    "registrationEnd": [date],
    "maxTeams": [int],
    "backdrop": [str, type(None)],
    "icon": [str, type(None)]
}

returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["gameId"] = [int]

class Games(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.permission.missingPermission, errorList.data.doesNotExist])
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
                return GameModel.getAllDict(), 200
            else:
                raise errorList.permission.missingPermission
        else:
            if perms.game.read:
                game = getGame(gameId)
                return game.toDict(), 200
            else:
                raise errorList.permission.missingPermission

    @postJson(accessibleAttributes)
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @hasPermissionDecorator(perms.game.update, True)
    def put(self, gameId, data, authResult: AuthResult, permissions: List[str]):
        """Updates game

        Args:
            gameId (str): id of the game

        Returns:
            dict: info about game
        """
        game = getGame(gameId)
        setAttributeFromList(game, data, accessibleAttributes)
        return game.toDict()

    @returnParser({"gameId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.data.stillDepends])
    @hasPermissionDecorator(perms.game.delete, True)
    def delete(self, gameId, authResult: AuthResult, permissions: List[str]):
        """Deletes game

        Args:
            gameId (str): id of the game

        Returns:
            dict: info about game
        """
        game = getGame(gameId)
        try:
            game.delete()
        except DatabaseError as e:
            raise errorList.data.stillDepends
        return {"gameId": game.gameId}, 200

gamePageAccessibleAttributes = {
    "gamePage": [str]
}

gamePageReturnableAttributes = deepcopy(accessibleAttributes)
gamePageReturnableAttributes["gameId"] = [int]

class GamePage(Resource):
    @returnParser(gamePageReturnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist])
    @hasPermissionDecorator(perms.gamePage.read, True)
    def get(self, gameId, authResult: AuthResult, permissions: List[str]):
        """Gets gamepage

        Args:
            gameId (str): id of the game

        Returns:
            dict: gameid and gamepage
        """
        game = getGame(gameId)
        gamePage = game.getGamePage()
        return {"game_id": gameId, "gamePage": gamePage}

    @returnParser(gamePageReturnableAttributes, 200, False)
    @returnError([errorList.data.doesNotExist])
    @postJson(gamePageAccessibleAttributes)
    @hasPermissionDecorator(perms.gamePage.update, True)
    def put(self, data, authResult: AuthResult, permissions: List[str], gameId):
        """Updates gamepage

        Args:
            gameId (str): id of the game

        Returns:
            None:
        """
        game = getGame(gameId)
        game.gamePage = data["gamePage"]
        return {"game_id": game.gameId, "gamePage": game.getGamePage()}

class CreateGame(Resource):
    @returnParser(returnableAttributes, 201, False, False)
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator([perms.game.create], False)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates games

        Args:

        Returns:
            dict: info about games
        """

        game = GameModel.create(data["name"], data["registrationStart"], data["registrationEnd"], data["maxTeams"], data["backdrop"], data["icon"]).toDict()

        return game, 201
