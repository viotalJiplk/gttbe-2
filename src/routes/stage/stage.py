from flask_restx import Resource
from shared.models.stage import StageModel
from utils.role import getRole
from utils.jws import jwsProtected, AuthResult
from utils.others import postJsonParse, postJson, setAttributeFromList
from datetime import datetime
from shared.models.role import RoleModel
from shared.models.event import EventModel
from utils.error import handleReturnableError
from shared.models.permission import hasPermission
from helper.event import getEvent
from helper.stage import getStage
from helper.user import getUser
from shared.utils.permissionList import perms
from utils.errorList import errorList

accessibleAttributes = {
    "eventId": [int],
    "stageName": [str],
    "stageIndex": [int],
}

class Stages(Resource):
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, stageId: str):
        """Gets stage

        Args:
            stageId (str): id of stage

        Returns:
            dict: info about stage
        """
        user = getUser(authResult)
        stage = getStage(stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.stage.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return stage.toDict()

    @handleReturnableError
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, stageId: str):
        """Deletes stage

        Args:
            stageId (str): id of stage

        Returns:
            None:
        """
        user = getUser(authResult)
        stage = getStage(stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.stage.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            stage.delete()
        except e:
            raise errorList.data.stillDepends
        return

    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson
    def put(self, data, authResult: AuthResult, stageId: str):
        """Updates stage

        Args:
            stageId (str): id of stage

        Returns:
            dict: info about stage
        """
        user = getUser(authResult)
        stage = getStage(stageId)
        event = getEvent(stage.eventId)
        permission = hasPermission(user, event.gameId, perms.stage.update)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        setAttributeFromList(stage, data, accessibleAttributes)
        return stage.toDict()

class StageCreate(Resource):
    @handleReturnableError
    @jwsProtected(optional=True)
    @postJsonParse(expectedJson=accessibleAttributes)
    def post(self, data, authResult: AuthResult):
        """Creates stage

        Args:

        Returns:
            dict: info about stage
        """
        user = getUser(authResult)
        event = getEvent(data["eventId"])
        permission = hasPermission(user, event.gameId, perms.stage.create)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return StageModel.create(data["eventId"], data["stageName"], data["stageIndex"]).toDict()
