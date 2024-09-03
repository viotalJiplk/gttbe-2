from flask_restx import Resource
from shared.models import GeneratedRoleModel, hasPermission
from shared.utils import perms, DatabaseError
from helper import getGeneratedRole, getUser
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, handleReturnableError, jwsProtected
from typing import List

accessibleAttributes = {
    "roleName": [str],
    "discordRoleId": [int, type(None)],
    "discordRoleIdEligible": [int, type(None)],
    "gameId": [int],
    "default": [bool],
    "minimal": [int],
    "maximal": [int]
}

class GeneratedRoles(Resource):
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, generatedRoleId: str):
        """Gets generatedRole

        Args:
            generatedRoleId (str): id of generatedRole

        Returns:
            dict: info about generatedRole
        """
        user = getUser(authResult)
        generatedRole = getGeneratedRole(generatedRoleId)
        permission = hasPermission(user, generatedRole.gameId, perms.generatedRole.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return generatedRole.toDict()

    @handleReturnableError
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, generatedRoleId: str):
        """Deletes generatedRole

        Args:
            generatedRoleId (str): id of generatedRole

        Returns:
            None:
        """
        user = getUser(authResult)
        generatedRole = getGeneratedRole(generatedRoleId)
        permission = hasPermission(user, generatedRole.gameId, perms.generatedRole.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            return generatedRole.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise

    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson
    def put(self, data, authResult: AuthResult, generatedRoleId: str):
        """Updates generatedRole

        Args:
            generatedRoleId (str): id of generatedRole

        Returns:
            dict: info about generatedRole
        """
        user = getUser(authResult)
        generatedRole = getGeneratedRole(generatedRoleId)
        permissionOld = hasPermission(user, generatedRole.gameId, perms.generatedRole.update)
        if len(permissionOld) < 1:
            raise errorList.permission.missingPermission
        if "gameId" in data:
            permissionNew = hasPermission(user, data["gameId"], perms.generatedRole.update)
            if len(permissionNew) < 1:
                raise errorList.permission.missingPermission
        setAttributeFromList(generatedRole, data, accessibleAttributes)
        return generatedRole.toDict()

class GeneratedRolesCreate(Resource):
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator([perms.generatedRole.create], True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates generatedRole

        Args:

        Returns:
            dict: info about generatedRole
        """
        return GeneratedRoleModel.create(data["roleName"], data["discordRoleId"], data["discordRoleIdEligible"], data["gameId"], data["default"], data["minimal"], data["maximal"]).toDict()
