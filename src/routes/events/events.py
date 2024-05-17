from flask_restful import Resource
from models.event import EventModel
from utils.role import getRole
from utils.jws import jwsProtected
from utils.utils import postJsonParse
from datetime import datetime
from models.role import RoleModel

class Events(Resource):
    def get(self, eventId):
        event = EventModel.getById(eventId=eventId)
        event.description = "xd"
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        return event.toDict()
    @jwsProtected()
    def delete(self, authResult, eventId):
        event = EventModel.getById(eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        event.delete()
        return 

class EventCreate(Resource):
    @jwsProtected()
    @postJsonParse(expectedJson={
        "date": [str],
        "beginTime": [str],
        "endTime": [str],
        "gameId": [int],
        "description": [str],
        "eventType": [str, type(None)]
    })
    @getRole(roleArray=["admin"], optional=False)
    def post(self, data, authResult, hasRole):
        date = datetime.strptime(data["date"], "%Y-%m-%d").date()
        beginTime = datetime.strptime(data["beginTime"], "%H:%M:%S").time()
        endTime = datetime.strptime(data["endTime"], "%H:%M:%S").time()
        return EventModel.create(date, beginTime, endTime, data["gameId"], data["description"], data["eventType"]).toDict()

class EventList(Resource):
    def get(self):
        return EventModel.getAllDict()