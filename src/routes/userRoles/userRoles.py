from flask_restx import Resource
from shared.models import UserRoleModel
from shared.utils import perms, DatabaseError
from helper import getUserRole
from utils import hasPermissionDecorator, AuthResult, postJsonParse, postJson, setAttributeFromList, errorList, returnParser, returnError
from typing import List
from copy import deepcopy

accessibleAttributes = {
    "assignedRoleId": [int],
    "userId": [int],
}
returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["userRoleId"] = [int]

class UserRoles(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist])
    @hasPermissionDecorator([perms.userRole.read], False)
    def get(self, authResult: AuthResult, userRoleId: str, permissions: List[str]):
        """Gets userRole

        Args:
            userRoleId (str): id of userRole

        Returns:
            dict: info about userRole
        """
        userRole = getUserRole(userRoleId)
        return userRole.toDict()

    @returnParser({"userRoleId": [int]})
    @returnError([errorList.data.doesNotExist, errorList.data.stillDepends])
    @hasPermissionDecorator([perms.userRole.delete], False)
    def delete(self, authResult: AuthResult, userRoleId: str, permissions: List[str]):
        """Deletes userRole

        Args:
            userRoleId (str): id of userRole

        Returns:
            None:
        """
        userRole = getUserRole(userRoleId)
        try:
            userRole.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise
        return {"userRoleId": userRole.userRoleId}

    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.doesNotExist, errorList.data.couldNotConvertInt, errorList.data.unableToConvert])
    @hasPermissionDecorator([perms.userRole.update], False)
    @postJson(accessibleAttributes)
    def put(self, data, authResult: AuthResult, userRoleId: str, permissions: List[str]):
        """Updates userRole

        Args:
            userRoleId (str): id of userRole

        Returns:
            dict: info about userRole
        """
        userRole = getUserRole(userRoleId)
        setAttributeFromList(userRole, data, accessibleAttributes)
        return userRole.toDict()

class UserRolesCreate(Resource):
    @returnParser(returnableAttributes, 200, False, False)
    @returnError([errorList.data.alreadyExists])
    @hasPermissionDecorator([perms.userRole.create], False)
    @postJsonParse(expectedJson=accessibleAttributes)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates userRole

        Args:

        Returns:
            dict: info about userRole
        """
        try:
            newAssignedRolePermission = UserRoleModel.create(data["assignedRoleId"], data["userId"]).toDict()
        except ValueError as e:
            if e.msg == "assignedRole already has this permission":
                raise errorList.data.alreadyExists
            else:
                raise
        return newAssignedRolePermission, 201
