from flask_restx import Resource
from shared.models import EventModel, hasPermission
from helper import getEvent, getStage, getUser
from utils import handleReturnableError, jwsProtected, errorList, AuthResult
from shared.utils import perms

class MatchesList(Resource):
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, stageId):
        """
            Lists all matches of event
        Args:
            eventId (str): id of event

        Returns:
            dict: list of matches
        """
        user = getUser(authResult)
        stage = getStage(stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.stage.listMatches)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return stage.allMatchesDict()
