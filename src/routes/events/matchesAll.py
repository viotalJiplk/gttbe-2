from flask_restx import Resource
from shared.models import EventModel
from utils import handleReturnableError
from utils import jwsProtected

class MatchesList(Resource):
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, eventId):
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
