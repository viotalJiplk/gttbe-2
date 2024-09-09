from flask_restx import Resource
from shared.models import StageModel, hasPermission
from utils import jwsProtected, AuthResult, postJsonParse, postJson, setAttributeFromList, handleReturnableError, errorList, hasPermissionDecorator
from helper import getEvent, getStage, getUser
from shared.utils import perms

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
    @postJson(accessibleAttributes)
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

class StageListAll(Resource):
    @hasPermissionDecorator(perms.stage.listAll, False)
    def get(self, authResult: AuthResult, permissions):
        """List all stages

        Args:

        Returns:
            dict: list of all stages
        """
        return StageModel.getAllDict()
