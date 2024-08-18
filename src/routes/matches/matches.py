from flask_restx import Resource
from shared.models.stage import StageModel
from utils.jws import jwsProtected, AuthResult
from utils.others import postJsonParse, postJson, setAttributeFromList
from datetime import datetime
from shared.models.event import EventModel
from shared.models.match import MatchModel
from utils.error import handleReturnableError
from shared.models.permission import hasPermission
from helper.event import getEvent
from helper.stage import getStage
from helper.user import getUser
from helper.match import getMatch
from shared.utils.permissionList import perms
from utils.errorList import errorList

accessibleAttributes = {
    "stageId": [int],
    "firstTeamId": [int],
    "secondTeamId": [int],
    "firstTeamResult": [int],
    "secondTeamResult": [int],
}

class Matches(Resource):
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
        except e:
            return {"kind": "DATA", "msg": "There are still data, that is dependent on this."}, 401
        return

    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson
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
        return MatchModel.create(data["stageId"], data["firstTeamId"], data["secondTeamId"], data["firstTeamResult"], data["secondTeamResult"]).toDict()
