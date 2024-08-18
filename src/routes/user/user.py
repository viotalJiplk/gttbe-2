from flask_restx import Resource
from shared.models.user import UserModel
from shared.models.team import TeamModel
from utils.jws import jwsProtected, AuthResult
from shared.utils.permissionList import perms
from utils.others import postJson, setAttributeFromList
from helper.user import getUser
from utils.errorList import errorList
from utils.permissions import hasPermissionDecorator
from typing import List

accessibleAttributes = {
    "surname": [str],
    "name": [str],
    "adult": [bool],
    "schoolId": [int],
}

class UserEndpoint(Resource):
    @hasPermissionDecorator([perms.user.readMe, perms.user.read], False)
    def get(self, authResult:AuthResult, uid: str, permissions: List[str]):
        """Gets info about user
            For non admin accounts only <userId> = @me is allowed.

        Args:
            uid (str): discordId of user

        Returns:
            dict: info about user
        """
        user = None
        if uid == '@me':
            if perms.user.readMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.read not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(uid, None))
        return user.toDict()

    @postJson
    @hasPermissionDecorator([perms.user.updateMe, perms.user.update], False)
    def put(self, data, authResult:AuthResult, uid: str, permissions: List[str]):
        """Updates info about user
            For non admin accounts only <userId> = @me is allowed.
        Args:
            uid (str): discordId of user

        Returns:
            None:
        """
        user = None
        if uid == '@me':
            if perms.user.updateMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.update not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(uid, None))
        setAttributeFromList(user, data, accessibleAttributes)
        return user.toDict()

    @hasPermissionDecorator([perms.user.deleteMe, perms.user.delete], False)
    def delete(self, authResult:AuthResult, uid: str, permissions: List[str]):
        """Deletes user
            For non admin accounts only <userId> = @me is allowed.

        Args:
            uid (str): discordId of user

        Returns:
            None:
        """
        user = None
        if uid == '@me':
            if perms.user.deleteMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.delete not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(uid, None))
        try:
            user.delete()
        except e:
            raise errorList.data.stillDepends
        return {}, 200

class UserExistsEndpoint(Resource):
    @hasPermissionDecorator(perms.user.exists, False)
    def get(self, authResult:AuthResult, uid: str, permissions: List[str]):
        """Tests if user exists in db

        Args:
            uid (str): discordId of user

        Returns:
            dict: exists
        """
        return {"exists": UserModel.getById(uid) is not None}

class UserPermissions(Resource):
    @hasPermissionDecorator([perms.user.permissionList, perms.user.permissionListMe], True)
    def get(self, authResult:AuthResult, uid: str, gameId: str, permissions: List[str]):
        """Returns users permissions for specific game

        Args:
            uid (str): userId (can be @me)
            gameId (str): gameId (can be all = permission for all games)

        Returns:
            List[str]: permission list
        """
        user = None
        if uid == '@me':
            if perms.user.permissionListMe not in permissions:
                raise errorList.permission.missingPermission
            if authResult.userId is None:
                raise errorList.request.missingHeaderForMe
            user = getUser(authResult)
        else:
            if perms.user.permissionList not in permissions:
                raise errorList.permission.missingPermission
            user = getUser(AuthResult(uid, None))
        if gameId == "all":
            gameId = None
        userPerms = user.listPermissions(gameId)
        return userPerms

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
