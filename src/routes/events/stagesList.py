from flask_restx import Resource
from shared.models import EventModel, hasPermission
from helper import getEvent, getUser
from utils import handleReturnableError, jwsProtected, errorList, AuthResult, returnParser, returnError
from shared.utils import perms

returnableAttributes = {
    "stageId": [int],
    "eventId": [int],
    "stageName": [str],
    "stageIndex": [int]
  }

class StagesList(Resource):
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
        permission = hasPermission(user, event.gameId, perms.event.listStages)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return event.listStages()
