from flask_restful import Resource, request
from models.user import UserModel
from utils.jws import authorize


class UserEndpoint(Resource):
    def get(self, uid):
        if(uid == '@me'):
            auth_result = authorize(request)
            user = UserModel.getById(auth_result["userid"])
            return {"discord_user_object": user.getDiscordUserObject()}
        else:
            return {"msg":"admin section! to be implemented"}
    def delete(self, uid):
        if(uid == '@me'):
            try:
                auth_result = authorize(request)
                user = UserModel.getById(auth_result["userid"])
                user.delete()
            except:
                return 401
            return 200
        else:
            return {"msg":"admin section! to be implemented"}