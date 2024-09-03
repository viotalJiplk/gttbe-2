from flask_restx import Resource
from shared.models import AssignedRolePermissionModel, hasPermission
from shared.utils import perms, DatabaseError
from helper import getAssignedRolePermission, getUser
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, handleReturnableError, jwsProtected
from typing import List

accessibleAttributes = {
    "permission": [str],
    "gameId": [int, type(None)],
    "assignedRoleId": [int],
}

class AssignedRolePermissions(Resource):
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
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, assignedRolePermissionId: str):
        """Deletes assignedRolePermission

        Args:
            assignedRolePermissionId (str): id of assignedRolePermission

        Returns:
            None:
        """
        user = getUser(authResult)
        assignedRolePermission = getAssignedRolePermission(assignedRolePermissionId)
        permission = hasPermission(user, assignedRolePermission.gameId, perms.assignedRolePermission.delete)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        try:
            return assignedRolePermission.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise

    @handleReturnableError
    @jwsProtected(optional=True)
    @postJson
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
    @postJsonParse(expectedJson=accessibleAttributes)
    @hasPermissionDecorator([perms.assignedRolePermission.create], True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates assignedRolePermission

        Args:

        Returns:
            dict: info about assignedRolePermission
        """
        return AssignedRolePermissionModel.create(data["permission"], data["assignedRoleId"], data["gameId"]).toDict()
