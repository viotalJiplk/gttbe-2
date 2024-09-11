from flask_restx import Resource
from utils import jwsProtected, AuthResult, postJsonParse, postJson, setAttributeFromList, handleReturnableError, errorList, hasPermissionDecorator, returnParser, returnError
from datetime import datetime
from shared.models import EventModel, MatchModel, hasPermission, StageModel
from helper import getEvent, getStage, getUser, getMatch
from shared.utils import perms
from copy import deepcopy

accessibleAttributes = {
    "stageId": [int],
    "firstTeamId": [int],
    "secondTeamId": [int],
    "firstTeamResult": [int],
    "secondTeamResult": [int],
}
returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["matchId"] = [int]

class Matches(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, matchId:str):
        """Gets Match

        Args:
            matchId (str): id of match

        Returns:
            dict: info about match
        """
        user = getUser(authResult)
        match = getMatch(matchId)
        stage = getStage(match.stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.match.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return match.toDict()

    @handleReturnableError
    @returnParser({"matchId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.stillDepends])
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, matchId:str):
        """Deletes match

        Args:
            matchId (str): id of match

        Returns:
            None:
        """
        user = getUser(authResult)
        match = getMatch(matchId)
        stage = getStage(match.stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.match.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            match.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise
        return {"matchId": match.matchId}

    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson(accessibleAttributes)
    def put(self, data, authResult: AuthResult, matchId:str):
        """Updates match

        Args:
            matchId (str): id of match

        Returns:
            dict: info about match
        """
        user = getUser(authResult)
        match = getMatch(matchId)
        stage = getStage(match.stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.match.update)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        setAttributeFromList(match, data, accessibleAttributes)
        return match.toDict()

class MatchCreate(Resource):
    @returnParser(returnableAttributes, 201, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    @postJsonParse(expectedJson=accessibleAttributes)
    def post(self, data, authResult: AuthResult):
        """Creates match

        Args:

        Returns:
            dict: info about match
        """
        user = getUser(authResult)
        stage = getStage(data["stageId"])
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.match.create)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return MatchModel.create(data["stageId"], data["firstTeamId"], data["secondTeamId"], data["firstTeamResult"], data["secondTeamResult"]).toDict(), 201

class MatchListAll(Resource):
    @returnParser(returnableAttributes, 200, True, False)
    @hasPermissionDecorator(perms.match.listAll, False)
    def get(self, authResult: AuthResult, permissions):
        """List all matches

        Args:

        Returns:
            dict: list of all matches
        """
        return MatchModel.getAllDict()
