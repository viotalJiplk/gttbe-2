from flask_restful import Resource
from models.event import EventModel

class MatchesList(Resource):
    def get(self, eventId):
        event = EventModel.getById(eventId)
        return event.allMatchesDict()
