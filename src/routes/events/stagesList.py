from flask_restx import Resource
from shared.models import EventModel, hasPermission
from helper import getEvent, getUser
from utils import handleReturnableError, jwsProtected, errorList, AuthResult
from shared.utils import perms

class StagesList(Resource):
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
