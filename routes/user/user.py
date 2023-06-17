from flask_restful import Resource, request
from models.user import UserModel
from utils.jws import jwsProtected


class UserEndpoint(Resource):

    @jwsProtected()
    def get(self, authResult, uid):
        if(uid == '@me'):
            user = UserModel.getById(authResult["userId"])
            return {"discord_user_object": user.getDiscordUserObject()}
        else:
            return {"msg":"admin section! to be implemented"}

    @jwsProtected()
    def delete(self, authResult, uid):
        if(uid == '@me'):
            try:
                user = UserModel.getById(authResult["userId"])
                user.delete()
            except:
                return 401
            return 200
        else:
            return {"msg":"admin section! to be implemented"}