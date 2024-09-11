from flask_restx import Resource
from shared.models import GeneratedRoleModel, hasPermission
from shared.utils import perms, DatabaseError
from helper import getGeneratedRole, getUser
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, handleReturnableError, jwsProtected, returnParser, returnError
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "roleName": [str],
    "discordRoleId": [int, type(None)],
    "discordRoleIdEligible": [int, type(None)],
    "gameId": [int],
    "default": [bool],
    "minimal": [int],
    "maximal": [int]
}
returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["generatedRoleId"] = [int]

class GeneratedRoles(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
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
    @returnParser({"generatedRoleId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.stillDepends])
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
            generatedRole.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise
        return {"generatedRoleId": generatedRole.generatedRoleId}

    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson(accessibleAttributes)
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
    @returnParser(returnableAttributes, 201, False, False)
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator([perms.generatedRole.create], True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates generatedRole

        Args:

        Returns:
            dict: info about generatedRole
        """
        try:
            newGeneratedRoleModel = GeneratedRoleModel.create(data["roleName"], data["discordRoleId"], data["discordRoleIdEligible"], data["gameId"], data["default"], data["minimal"], data["maximal"]).toDict()
        except ValueError as e:
            if e.msg == "Role with this name already exists":
                errorList.data.alreadyExists
            else:
                raise
        return newGeneratedRoleModel, 201

class GeneratedRoleList(Resource):
    @returnParser(returnableAttributes, 200, True, False)
    @hasPermissionDecorator([perms.generatedRole.listAll], True)
    def get(self, authResult: AuthResult, gameId: int, permissions):
        """lists generatedRoles

        Args:
            gameId (int): id of game or all

        Returns:
            dict: list of generated roles
        """
        if gameId == "all":
            return GeneratedRoleModel.getAllDict(gameId=None)
        else:
            return GeneratedRoleModel.getAllDict(gameId=gameId)


class GeneratedRolePermissions(Resource):
    @returnParser({
        "generatedRolePermissionId": [int],
        "permission": [str],
        "generatedRoleId": [int],
        "gameId": [int],
        "eligible": [int]
    }, 200, True, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, generatedRoleId: str):
        """Gets generatedRoles permissions

        Args:
            generatedRoleId (str): id of generatedRole

        Returns:
            dict: list of generated role permissions
        """
        user = getUser(authResult)
        generatedRole = getGeneratedRole(generatedRoleId)
        permission = hasPermission(user, generatedRole.gameId, perms.generatedRole.listPermissions)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return generatedRole.listPermissions()
