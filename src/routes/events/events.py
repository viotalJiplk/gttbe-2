from flask_restful import Resource
from models.event import EventModel

class EventList(Resource):
    def get(self):
        return EventModel.getAllDict() 