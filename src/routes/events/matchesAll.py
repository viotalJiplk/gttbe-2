from flask_restx import Resource
from shared.models import EventModel, hasPermission
from helper import getEvent, getUser
from utils import handleReturnableError, jwsProtected, errorList, AuthResult, returnParser, returnError
from shared.utils import perms
from datetime import time, date

returnableAttributes = {
    "matchId": [int],
    "stageId": [int],
    "firstTeamId": [int],
    "secondTeamId": [int],
    "firstTeamResult": [int, type(None)],
    "secondTeamResult": [int, type(None)],
    "eventId": [int],
    "stageName": [str],
    "stageIndex": [int],
    "date": [date],
    "beginTime": [time],
    "endTime": [time],
    "gameId": [int],
    "description": [str],
    "eventType": [str]
  }

class MatchesList(Resource):
    @returnParser(returnableAttributes, 200, True, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, eventId):
        """
            Lists all matches of event
        Args:
            eventId (str): id of event

        Returns:
            dict: list of matches
        """
        user = getUser(authResult)
        event = getEvent(eventId)
        permission = hasPermission(user, event.gameId, perms.event.listMatches)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return event.allMatchesDict()
