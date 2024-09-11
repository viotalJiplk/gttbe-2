from flask_restx import Resource, fields
from shared.models import AssignedRolePermissionModel, hasPermission
from shared.utils import perms, DatabaseError
from helper import getAssignedRolePermission, getUser
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, handleReturnableError, jwsProtected, returnParser, errorList, returnError
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "permission": [str],
    "gameId": [int, type(None)],
    "assignedRoleId": [int],
}

returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["assignedRolePermissionsId"] = [int]

class AssignedRolePermissions(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission])
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, assignedRolePermissionId: str):
        """Gets assignedRolePermission

        Args:
            assignedRolePermissionId (str): id of assignedRolePermission

        Returns:
            dict: info about assignedRolePermission
        """
        user = getUser(authResult)
        assignedRolePermission = getAssignedRolePermission(assignedRolePermissionId)
        permission = hasPermission(user, assignedRolePermission.gameId, perms.assignedRolePermission.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        return assignedRolePermission.toDict()

    @handleReturnableError
    @returnParser({"assignedRolePermissionId": [int]}, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.stillDepends])
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, assignedRolePermissionId: str):
        """Deletes assignedRolePermission

        Args:
            assignedRolePermissionId (str): id of assignedRolePermission

        Returns:
            dict: assignedRolePermissionId
        """
        user = getUser(authResult)
        assignedRolePermission = getAssignedRolePermission(assignedRolePermissionId)
        permission = hasPermission(user, assignedRolePermission.gameId, perms.assignedRolePermission.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            assignedRolePermission.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise
        return {"assignedRolePermissionId": assignedRolePermission.assignedRolePermissionId}

    @handleReturnableError
    @jwsProtected(optional=True)
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.permission.missingPermission, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @postJson(accessibleAttributes)
    def put(self, data, authResult: AuthResult, assignedRolePermissionId: str):
        """Updates assignedRolePermission

        Args:
            assignedRolePermissionId (str): id of assignedRolePermission

        Returns:
            dict: info about assignedRolePermission
        """
        user = getUser(authResult)
        assignedRolePermission = getAssignedRolePermission(assignedRolePermissionId)
        permissionOld = hasPermission(user, assignedRolePermission.gameId, perms.assignedRolePermission.update)
        if len(permissionOld) < 1:
            raise errorList.permission.missingPermission
        if "gameId" in data:
            permissionNew = hasPermission(user, data["gameId"], perms.assignedRolePermission.update)
            if len(permissionNew) < 1:
                raise errorList.permission.missingPermission
        setAttributeFromList(assignedRolePermission, data, accessibleAttributes)
        return assignedRolePermission.toDict()

class AssignedRolePermissionsCreate(Resource):
    @returnParser(returnableAttributes, 201, False, False)
    @returnError([errorList.data.alreadyExists])
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator([perms.assignedRolePermission.create], True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates assignedRolePermission

        Args:

        Returns:
            dict: info about assignedRolePermission
        """
        try:
            newAssignedRolePermission = AssignedRolePermissionModel.create(data["permission"], data["assignedRoleId"], data["gameId"]).toDict()
        except ValueError as e:
            if e.msg == "assignedRole already has this permission":
                raise errorList.data.alreadyExists
            else:
                raise
        return newAssignedRolePermission, 201
