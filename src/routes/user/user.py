from flask_restx import Resource
from models.user import UserModel
from utils.jws import jwsProtected
from models.role import RoleModel
from utils.role import hasRoleWithErrMsg
from models.user import UserModel
from utils.utils import postJson

class UserEndpoint(Resource):

    @jwsProtected()
    def get(self, authResult, uid):
        """Gets info about user
            For non admin accounts only <userId> = @me is allowed.

        Args:
            uid (str): discordId of user

        Returns:
            dict: info about user
        """
        if uid == '@me':
            return UserModel.getById(authResult["userId"]).toDict()
        else:
            result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
            if result is True:
                return UserModel.getById(uid).toDict()
            else:
                return result

    @jwsProtected()
    @postJson
    def put(self, data, authResult, uid):
        """Updates info about user
            For non admin accounts only <userId> = @me is allowed.
        Args:
            uid (str): discordId of user

        Returns:
            None:
        """
        if("name" not in data):
            data["name"] = ''
        if("surname" not in data):
            data["surname"] = ''
        if("adult" not in data):
            data["adult"] = ''
        if("school_id" not in data):
            data["school_id"] = ''
        try:
            if(uid == '@me'):
                UserModel.updateOrCreateUser(userid=authResult["userId"], refresh_token='', access_token='',  expires_in='', name=data["name"], surname=data["surname"], adult=data["adult"], school_id=data["school_id"])
                return {}, 205
            else:
                result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
                if result is True:
                    UserModel.updateOrCreateUser(userid=authResult["userId"], refresh_token='', access_token='',  expires_in='', name=data["name"], surname=data["surname"], adult=data["adult"], school_id=data["school_id"])
                    return {}, 205
                else:
                    return result
        except:
            return {"kind": "USER", "msg": "User does not exist or there was nothing to change."}, 404

    @jwsProtected()
    def delete(self, authResult, uid):
        """Deletes user
            For non admin accounts only <userId> = @me is allowed.

        Args:
            uid (str): discordId of user

        Returns:
            None:
        """
        if(uid == '@me'):
            try:
                user = UserModel.getById(authResult["userId"])
                user.delete()
            except:
                return {"kind": "USER", "msg": "You are registered in team or you play active role in management."}, 403
            return {}, 200
        else:
            result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
            if result is True:
                try:
                    user = UserModel.getById(uid)
                    user.delete()
                    return {}, 200
                except:
                    return {}, 403
            else:
                return result

class UserExistsEndpoint(Resource):
    def get(self, uid):
        """Tests if user exists in db

        Args:
            uid (str): discordId of user

        Returns:
            dict: exists
        """
        return {"exits": UserModel.getById(uid) is not None}
