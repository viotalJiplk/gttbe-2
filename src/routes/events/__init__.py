from routes.discord.auth import Auth, TokenEndpoint
from flask_restful import Resource, request
from routes.events.events import EventList, EventCreate, Events

class EventDescr(Resource):
    def get(self):
        return [
            {
                "name": "list",
                "url": "list/",
                "type": "public",
                "method": "GET",
                "descr": "Gets all events."
            }
        ], 200

eventRoutes = [(EventDescr, '/'), (EventList, '/list'), (EventCreate, '/create'), (Events, '/<eventId>/')]