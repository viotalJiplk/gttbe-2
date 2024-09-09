from flask_restx import Resource
from shared.models import AssignedRoleModel
from shared.utils import perms, DatabaseError
from helper import getAssignedRole
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList
from typing import List

accessibleAttributes = {
    "roleName": [str],
    "discordRoleId": [int, type(None)],
}

class AssignedRoles(Resource):
    @hasPermissionDecorator([perms.assignedRole.read], False)
    def get(self, authResult: AuthResult, assignedRoleId: str, permissions: List[str]):
        """Gets assignedRole

        Args:
            assignedRoleId (str): id of assignedRole

        Returns:
            dict: info about assignedRole
        """
        assignedRole = getAssignedRole(assignedRoleId)
        return assignedRole.toDict()

    @hasPermissionDecorator([perms.assignedRole.delete], False)
    def delete(self, authResult: AuthResult, assignedRoleId: str, permissions: List[str]):
        """Deletes assignedRole

        Args:
            assignedRoleId (str): id of assignedRole

        Returns:
            None:
        """
        assignedRole = getAssignedRole(assignedRoleId)
        try:
            return assignedRole.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise

    @hasPermissionDecorator([perms.assignedRole.update], False)
    @postJson(accessibleAttributes)
    def put(self, data, authResult: AuthResult, assignedRoleId: str, permissions: List[str]):
        """Updates assignedRole

        Args:
            assignedRoleId (str): id of assignedRole

        Returns:
            dict: info about assignedRole
        """
        assignedRole = getAssignedRole(assignedRoleId)
        setAttributeFromList(assignedRole, data, accessibleAttributes)
        return assignedRole.toDict()

class AssignedRolesCreate(Resource):
    @hasPermissionDecorator([perms.assignedRole.create], False)
    @postJsonParse(expectedJson=accessibleAttributes)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates assignedRole

        Args:

        Returns:
            dict: info about assignedRole
        """
        return AssignedRoleModel.create(data["roleName"], data["discordRoleId"]).toDict()

class AssignedRoleList(Resource):
    @hasPermissionDecorator([perms.assignedRole.listAll], False)
    def get(self, authResult: AuthResult, permissions):
        """lists assignedRoles

        Args:

        Returns:
            dict: list of assigned roles
        """
        return AssignedRoleModel.getAllDict()

class AssignedRolePermissions(Resource):
    @hasPermissionDecorator([perms.assignedRole.listPermissions], False)
    def get(self, authResult: AuthResult, assignedRoleId: str, permissions: List[str]):
        """Gets assignedRole permissions

        Args:
            assignedRoleId (str): id of assignedRole

        Returns:
            dict: assignedRole permissions
        """
        assignedRole = getAssignedRole(assignedRoleId)
        return assignedRole.listPermissions()
