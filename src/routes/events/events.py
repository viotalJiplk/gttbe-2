from flask_restx import Resource
from models.event import EventModel
from utils.role import getRole
from utils.jws import jwsProtected
from utils.utils import postJsonParse, postJson
from datetime import datetime
from models.role import RoleModel

accessibleAttributes = {
    "date": [str],
    "beginTime": [str],
    "endTime": [str],
    "gameId": [int],
    "description": [str],
    "eventType": [str, type(None)]
}

class Events(Resource):
    def get(self, eventId):
        """Gets event

        Args:
            eventId (str): id of event

        Returns:
            dict: info about event
        """
        event = EventModel.getById(eventId=eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        return event.toDict()
    @jwsProtected()
    def delete(self, authResult, eventId):
        """Deletes event

        Args:
            eventId (str): id of event

        Returns:
            None:
        """
        event = EventModel.getById(eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        try:
            event.delete()
        except e:
            return {"kind": "DATA", "msg": "There are still data, that is dependent on this."}, 401
        return

    @jwsProtected()
    @postJson
    def put(self, data, authResult, eventId):
        """Updates event

        Args:

        Returns:
            dict: info about event
        """
        event = EventModel.getById(eventId=eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin", "gameOrganizer"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        for x in data:
            if x in accessibleAttributes:
                if type(data[x]) in accessibleAttributes[x]:
                    if x == "beginTime" or x== "endTime":
                        final = datetime.strptime(data[x], "%H:%M:%S").time()
                        setattr(event, x, final)
                    elif x == "date":
                        final = datetime.strptime(data[x], "%Y-%m-%d").date()
                        setattr(event, x, final)
                    else:
                        setattr(event, x, data[x])

        return event.toDict()

class EventCreate(Resource):
    @jwsProtected()
    @postJsonParse(expectedJson=accessibleAttributes)
    @getRole(roleArray=["admin"], optional=False)
    def post(self, data, authResult, hasRole):
        """Creates event

        Args:

        Returns:
            dict: info about event
        """
        date = datetime.strptime(data["date"], "%Y-%m-%d").date()
        beginTime = datetime.strptime(data["beginTime"], "%H:%M:%S").time()
        endTime = datetime.strptime(data["endTime"], "%H:%M:%S").time()
        return EventModel.create(date, beginTime, endTime, data["gameId"], data["description"], data["eventType"]).toDict()

class EventList(Resource):
    def get(self):
        """Lists all events

        Returns:
            dict: List of events
        """
        return EventModel.getAllDict()
