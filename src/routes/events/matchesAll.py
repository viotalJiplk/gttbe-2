from flask_restx import Resource
from models.event import EventModel

class MatchesList(Resource):
    def get(self, eventId):
        """
            Lists all matches of event
        Args:
            eventId (str): id of event

        Returns:
            dict: list of matches
        """
        event = EventModel.getById(eventId)
        return event.allMatchesDict()
