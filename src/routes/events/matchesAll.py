from flask_restx import Resource
from shared.models.event import EventModel
from utils.error import handleReturnableError
from utils.jws import jwsProtected

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
