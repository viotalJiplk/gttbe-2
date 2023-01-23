from flask_restful import Resource, request
from models.user import UserModel

# todo add verification of inputs

class UserEndpoint:
    def post(self):
        try:
            data = request.get_json()
        except:
            return {"state": 1, "msg": "This is json endpoint."}, 401
        req = data
        if(data["userid"]==''):
           user = UserModel(data["user_id"])