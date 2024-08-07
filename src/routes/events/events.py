from flask_restx import Resource
from shared.models.event import EventModel
from utils.role import getRole
from utils.jws import jwsProtected, AuthResult
from datetime import datetime, date, time
from shared.models.role import RoleModel
from shared.models.permission import hasPermission
from shared.utils.permissionList import perms
from utils.permissions import hasPermissionDecorator
from utils.others import postJsonParse, postJson, setAttributeFromList
from utils.error import handleReturnableError
from helper.event import getEvent
from helper.user import getUser
from utils.errorList import errorList
from typing import List

accessibleAttributes = {
    "date": [date],
    "beginTime": [time],
    "endTime": [time],
    "gameId": [int],
    "description": [str],
    "eventType": [str, type(None)]
}

class Events(Resource):
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, eventId: str):
        """Gets event

        Args:
            eventId (str): id of event

        Returns:
            dict: info about event
        """
        user = getUser(authResult)
        event = getEvent(eventId)
        permission = hasPermission(user, event.gameId, perms.event.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return event.toDict()
    @handleReturnableError
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, eventId: str):
        """Deletes event

        Args:
            eventId (str): id of event

        Returns:
            None:
        """
        user = getUser(authResult)
        event = getEvent(eventId)
        permission = hasPermission(user, event.gameId, perms.event.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            event.delete()
        except e:
            raise errorList.data.stillDepends
        return

    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson
    def put(self, data, authResult: AuthResult, eventId: str):
        """Updates event

        Args:

        Returns:
            dict: info about event
        """
        user = getUser(authResult)
        event = getEvent(eventId)
        permission = hasPermission(user, event.gameId, perms.event.update)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        setAttributeFromList(event, data, accessibleAttributes)
        return event.toDict()

class EventCreate(Resource):
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator(perms.event.create, True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
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
    @hasPermissionDecorator(perms.event.listAll, False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all events

        Returns:
            dict: List of events
        """
        return EventModel.getAllDict()
