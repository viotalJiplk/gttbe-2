from flask_restx import Resource
from shared.models import RankModel, hasPermission
from utils import jwsProtected, AuthResult
from shared.utils import perms
from utils import hasPermissionDecorator, postJsonParse, postJson, setAttributeFromList, handleReturnableError, errorList, returnParser, returnError
from helper import getRank, getUser
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "rankName": [str],
    "gameId": [int],
}
returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["rankId"] = [int]

class Ranks(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, rankId: str):
        """Gets rank

        Args:
            rankId (str): id of event

        Returns:
            dict: info about event
        """
        user = getUser(authResult)
        rank = getRank(rankId)
        permission = hasPermission(user, rank.gameId, perms.rank.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return rank.toDict()

    @handleReturnableError
    @returnParser({"rankId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.stillDepends])
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, rankId: str):
        """Deletes event

        Args:
            rankId (str): id of event

        Returns:
            None:
        """
        user = getUser(authResult)
        rank = getRank(rankId)
        permission = hasPermission(user, rank.gameId, perms.rank.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            rank.delete()
        except e:
            raise errorList.data.stillDepends
        return {"rankId": rank.rankId}


    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson(accessibleAttributes)
    def put(self, data, authResult: AuthResult, rankId: str):
        """Updates rank

        Args:

        Returns:
            dict: info about rank
        """
        user = getUser(authResult)
        rank = getRank(rankId)
        permission = hasPermission(user, rank.gameId, perms.rank.update)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        setAttributeFromList(rank, data, accessibleAttributes)
        return rank.toDict()

class RankCreate(Resource):
    @returnParser(returnableAttributes, 201, False, False)
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator(perms.rank.create, True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates rank

        Args:

        Returns:
            dict: info about rank
        """
        return RankModel.create(data["rankName"], data["gameId"]).toDict(), 201

class RankList(Resource):
    @returnParser(returnableAttributes, 200, True, False)
    @hasPermissionDecorator(perms.rank.listRanks, True)
    def get(self, gameId: int, authResult: AuthResult, permissions: List[str]):
        """Lists all ranks

        Returns:
            dict: List of ranks
        """
        return RankModel.getDictByGame(gameId)
