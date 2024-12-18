from flask_restx import Resource
from shared.models import GeneratedRolePermissionModel, hasPermission
from shared.utils import perms, DatabaseError
from helper import getGeneratedRolePermission, getUser
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, handleReturnableError, jwsProtected, returnParser, returnError
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "permission": [str],
    "generatedRoleId": [int],
    "gameId": [int, type(None)],
    "eligible": [bool],
}

returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["generatedRolePermissionId"] = [int]

class GeneratedRolePermissions(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, generatedRolePermissionId: str):
        """Gets generatedRolePermission

        Args:
            generatedRolePermissionId (str): id of generatedRolePermission

        Returns:
            dict: info about generatedRolePermission
        """
        user = getUser(authResult)
        generatedRolePermission = getGeneratedRolePermission(generatedRolePermissionId)
        permission = hasPermission(user, generatedRolePermission.gameId, perms.generatedRolePermission.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return generatedRolePermission.toDict()

    @handleReturnableError
    @returnParser({"generatedRolePermissionId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.stillDepends])
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, generatedRolePermissionId: str):
        """Deletes generatedRolePermission

        Args:
            generatedRolePermissionId (str): id of generatedRolePermission

        Returns:
            None:
        """
        user = getUser(authResult)
        generatedRolePermission = getGeneratedRolePermission(generatedRolePermissionId)
        permission = hasPermission(user, generatedRolePermission.gameId, perms.generatedRolePermission.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            generatedRolePermission.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise
        return {"generatedRolePermissionId": generatedRolePermission.generatedRolePermissionId}

    @returnParser(returnableAttributes, 200, False, False)
    @handleReturnableError
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @jwsProtected(optional=True)
    @postJson(accessibleAttributes)
    def put(self, data, authResult: AuthResult, generatedRolePermissionId: str):
        """Updates generatedRolePermission

        Args:
            generatedRolePermissionId (str): id of generatedRolePermission

        Returns:
            dict: info about generatedRolePermission
        """
        user = getUser(authResult)
        generatedRolePermission = getGeneratedRolePermission(generatedRolePermissionId)
        permissionOld = hasPermission(user, generatedRolePermission.gameId, perms.generatedRolePermission.update)
        if len(permissionOld) < 1:
            raise errorList.permission.missingPermission
        if "gameId" in data:
            permissionNew = hasPermission(user, data["gameId"], perms.generatedRolePermission.update)
            if len(permissionNew) < 1:
                raise errorList.permission.missingPermission
        setAttributeFromList(generatedRolePermission, data, accessibleAttributes)
        return generatedRolePermission.toDict()

class GeneratedRolePermissionsCreate(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator([perms.generatedRolePermission.create], True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates generatedRolePermission

        Args:

        Returns:
            dict: info about generatedRolePermission
        """
        try:
            newGeneratedRolePermission = GeneratedRolePermissionModel.create(data["permission"], data["generatedRoleId"], data["gameId"], data["eligible"]).toDict()
        except ValueError as e:
            if e.msg == "generatedRole already has this permission":
                raise errorList.data.alreadyExists
            else:
                raise
        return newGeneratedRolePermission, 201
