from flask_restx import Resource
from shared.models import AssignedRoleModel
from shared.utils import perms, DatabaseError
from helper import getAssignedRole
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, returnParser, returnError
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "roleName": [str],
    "discordRoleId": [int, type(None)],
}

returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["assignedRoleId"] = [int]

class AssignedRoles(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist])
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
    @returnParser({"assignedRoleId": [int]}, 201, False, False)
    @returnError([errorList.data.doesNotExist, errorList.data.stillDepends])
    def delete(self, authResult: AuthResult, assignedRoleId: str, permissions: List[str]):
        """Deletes assignedRole

        Args:
            assignedRoleId (str): id of assignedRole

        Returns:
            None:
        """
        assignedRole = getAssignedRole(assignedRoleId)
        try:
            assignedRole.delete()
            return {"assignedRoleId": assignedRole.assignedRoleId}
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise

    @returnParser(returnableAttributes, 200, False, False)
    @hasPermissionDecorator([perms.assignedRole.update], False)
    @returnError([errorList.data.doesNotExist, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
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
    @returnParser(returnableAttributes, 200, False, False)
    @hasPermissionDecorator([perms.assignedRole.create], False)
    @postJsonParse(expectedJson=accessibleAttributes)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates assignedRole

        Args:

        Returns:
            dict: info about assignedRole
        """
        try:
            newAssignedRoleModel = AssignedRoleModel.create(data["roleName"], data["discordRoleId"]).toDict()
        except ValueError as e:
            if e.msg == "AssignedRole with this name already exists.":
                errorList.data.alreadyExists
            else:
                raise
        return newAssignedRoleModel, 201

class AssignedRoleList(Resource):
    @returnParser(returnableAttributes, 200, True, False)
    @hasPermissionDecorator([perms.assignedRole.listAll], False)
    def get(self, authResult: AuthResult, permissions):
        """lists assignedRoles

        Args:

        Returns:
            dict: list of assigned roles
        """
        return AssignedRoleModel.getAllDict()

class AssignedRolePermissionList(Resource):
    @returnParser({
        "permission": [str],
        "gameId": [int, type(None)],
        "assignedRoleId": [int],
    }, 200, True, False)
    @returnError([errorList.data.doesNotExist])
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
