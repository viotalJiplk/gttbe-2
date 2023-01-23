from flask_restful import Resource, request
from routes.discord.constants import *
from utils.errorlog import weberrorlog
from config import selfref
from routes.discord.api_connector import insertState, testState
from utils.jws import generateJWS
from models.user import UserModel
import json

class Auth(Resource):
    scopes = ["identify"]
    def get(self):
        state = insertState()
        if type(state) is dict:
            return weberrorlog(state["msg"], 500)
        return {"redirect_url": endpoint_url(state, "none")}, 200
        # could technicaly throw error if state is not unique

class TokenEndpoint(Resource):
    def post(self):
        try:
            data = request.get_json()
        except:
            return {"state": 1, "msg": "This is json endpoint."}, 401
        req = data
        if(data["code"] == '' or data["state"] == '' or data["redirect_uri"] == ''):
            return {"state": 1, "msg": "Missing something in request."}, 401
        if(testState(data["state"]) == False):
            return {"state": 1, "msg": "Invalid state."}, 401

        user = UserModel.getByCode(data["code"], data["redirect_uri"], data["name"], data["surname"], data["adult"], data["school_id"])

        claims = {}
        claims[selfref["root_url"] + "/discord/userid"] = user.userId
        jws = generateJWS(claims)
        
        return {"jws":jws}