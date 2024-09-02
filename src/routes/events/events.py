from flask_restx import Resource
from shared.models.event import EventModel
from utils import jwsProtected, AuthResult
from datetime import datetime, date, time
from shared.models import hasPermission
from shared.utils import perms
from utils import hasPermissionDecorator
from utils import postJsonParse, postJson, setAttributeFromList
from utils import handleReturnableError
from helper import getEvent
from helper import getUser
from utils import errorList
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
        return EventModel.create(data["date"], data["beginTime"], data["endTime"], data["gameId"], data["description"], data["eventType"]).toDict()

class EventList(Resource):
    @hasPermissionDecorator(perms.event.listAll, False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all events

        Returns:
            dict: List of events
        """
        return EventModel.getAllDict()
