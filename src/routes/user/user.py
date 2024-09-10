from flask_restx import Resource
from shared.models import UserModel, TeamModel
from utils import AuthResult, postJson, setAttributeFromList, errorList, hasPermissionDecorator
from shared.utils import perms, DatabaseError
from helper import getUser
from typing import List, Union
from copy import deepcopy

accessibleAttributes = {
    "surname": [str],
    "name": [str],
    "adult": [bool],
    "schoolId": [int],
}
returnableAttributes = deepcopy(accessibleAttributes)
returnableAttributes["userId"] = [int]

class UserEndpoint(Resource):
    @hasPermissionDecorator([perms.user.readMe, perms.user.read], False)
    def get(self, authResult:AuthResult, userId: str, permissions: List[str]):
        """Gets info about user
            For non admin accounts only <userId> = @me is allowed.

        Args:
            userId (str): discordId of user

        Returns:
            dict: info about user
        """
        user = None
        if userId == '@me':
            if perms.user.readMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.read not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        return user.toDict()

    @postJson(accessibleAttributes)
    @hasPermissionDecorator([perms.user.updateMe, perms.user.update], False)
    def put(self, data, authResult:AuthResult, userId: str, permissions: List[str]):
        """Updates info about user
            For non admin accounts only <userId> = @me is allowed.
        Args:
            userId (str): discordId of user

        Returns:
            None:
        """
        user = None
        if userId == '@me':
            if perms.user.updateMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.update not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        setAttributeFromList(user, data, accessibleAttributes)
        return user.toDict()

    @hasPermissionDecorator([perms.user.deleteMe, perms.user.delete], False)
    def delete(self, authResult:AuthResult, userId: str, permissions: List[str]):
        """Deletes user
            For non admin accounts only <userId> = @me is allowed.

        Args:
            userId (str): discordId of user

        Returns:
            None:
        """
        user = None
        if userId == '@me':
            if perms.user.deleteMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.delete not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        try:
            user.delete()
        except DatabaseError as e:
            if e.message == "Still depends":
                raise errorList.data.stillDepends
            else:
                raise
        return {}, 200

class UserExistsEndpoint(Resource):
    @hasPermissionDecorator(perms.user.exists, False)
    def get(self, authResult:AuthResult, userId: str, permissions: List[str]):
        """Tests if user exists in db

        Args:
            userId (str): discordId of user

        Returns:
            dict: exists
        """
        return {"exists": UserModel.getById(userId) is not None}

class UserPermissions(Resource):
    @hasPermissionDecorator([perms.user.permissionList, perms.user.permissionListMe], True)
    def get(self, authResult:AuthResult, userId: str, gameId:  Union[str], permissions: List[str]):
        """Returns users permissions for specific game

        Args:
            userId (str): userId (can be @me)
            gameId (str): gameId (can be all = permission for all games, any = permission for any game)

        Returns:
            List[str]: permission list
        """
        user = None
        if userId == '@me':
            if perms.user.permissionListMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.permissionList not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        if gameId == "all":
            gameId = None
        elif gameId == "any":
            gameId = True
        return user.listPermissions(gameId)

class UserGeneratedRoles(Resource):
    @hasPermissionDecorator([perms.user.generatedRolesList, perms.user.generatedRolesListMe], False)
    def get(self, authResult:AuthResult, userId: str, permissions: List[str]):
        """Returns list of users generatedRoles

        Args:
            userId (str): userId (can be @me)

        Returns:
            List[str]: list of generatedRoles
        """
        user = None
        if userId == '@me':
            if perms.user.generatedRolesListMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.generatedRolesList not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        return user.listGeneratedRoles()

class UserAssignedRoles(Resource):
    @hasPermissionDecorator([perms.user.assignedRolesList, perms.user.assignedRolesListMe], False)
    def get(self, authResult:AuthResult, userId: str, permissions: List[str]):
        """Returns list of users AssignedRoles

        Args:
            userId (str): userId (can be @me)

        Returns:
            List[str]: list of AssignedRoles
        """
        user = None
        if userId == '@me':
            if perms.user.assignedRolesListMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.assignedRolesList not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        return user.listAssignedRoles()

class ListTeam(Resource):
    @hasPermissionDecorator([perms.user.listTeamsMe, perms.user.listTeams], False)
    def get(self, authResult:AuthResult, userId: str, permissions: List[str]):
        """List teams user is currently in

        Args:
            userId (str): @me or id of user

        Returns:
            dict: list of teams
        """
        user = None
        withJoinString = False
        if userId == '@me':
            if perms.user.listTeamsMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
            withJoinString = True
        else:
            if perms.user.listTeams not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(userId, None))
        return TeamModel.listUsersTeams(user.userId, withJoinString), 200
