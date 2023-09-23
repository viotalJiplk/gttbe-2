from flask_restful import Resource, request
from models.user import UserModel
from utils.jws import jwsProtected
from models.role import RoleModel
from utils.role import hasRoleWithErrMsg

class UserEndpoint(Resource):

    @jwsProtected()
    def get(self, authResult, uid):
        if uid == '@me':
            return str(UserModel.getById(authResult["userId"]))
        else:
            result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
            if result is True:
                return str(UserModel.getById(uid))
            else:
                return result
            

    @jwsProtected()
    def delete(self, authResult, uid):
        if(uid == '@me'):
            try:
                user = UserModel.getById(authResult["userId"])
                user.delete()
            except:
                return 403
            return 200
        else:
            result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
            if result is True:
                try:
                    user = UserModel.getById(uid)
                    user.delete()
                except:
                    return 403
            else:
                return result

class UserExistsEndpoint(Resource):
    def get(self, uid):
        return {"exits": UserModel.getById(uid) is not None}