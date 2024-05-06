from flask_restful import Resource, request
from models.role import RoleModel
from utils.jws import jwsProtected
from utils.utils import postJson
from utils.role import getRole

class AddRole(Resource):

    @jwsProtected()
    @postJson
    @getRole(roleArray=["admin"], optional=False)
    def post(self, data, authResult, hasRole):
        if("game_id" not in data or "user_id" not in data or "role" not in data):
            return {"kind":"ROLE", "msg": "Missing game_id or user_id or role in data."}, 401
        try:
            RoleModel.create(data["user_id"], data["game_id"], data["role"])
        except ValueError as e:
            return {"kind":"ROLE", "msg": str(e)}, 401