from flask_restx import Resource
from shared.models import EventModel, hasPermission
from utils import jwsProtected, AuthResult
from datetime import datetime, date, time
from shared.utils import perms
from utils import hasPermissionDecorator, postJsonParse, postJson, setAttributeFromList, handleReturnableError, errorList, returnParser, returnError
from helper import getEvent, getUser
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "date": [date],
    "beginTime": [time],
    "endTime": [time],
    "gameId": [int],
    "description": [str],
    "eventType": [str, type(None)]
}
returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["eventId"] = [int]

class Events(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
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
    @returnParser({"eventId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.stillDepends])
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
        return {"eventId": event.eventId}


    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson(accessibleAttributes)
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
    @returnParser(returnableAttributes, 201, False, False)
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator(perms.event.create, True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates event

        Args:

        Returns:
            dict: info about event
        """
        return EventModel.create(data["date"], data["beginTime"], data["endTime"], data["gameId"], data["description"], data["eventType"]).toDict(), 201

class EventList(Resource):
    @returnParser(returnableAttributes, 200, True, False)
    @hasPermissionDecorator(perms.event.listAll, False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all events

        Returns:
            dict: List of events
        """
        return EventModel.getAllDict()
