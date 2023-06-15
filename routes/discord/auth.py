from flask_restful import Resource, request
from routes.discord.constants import *
from utils.errorlog import weberrorlog
from config import selfref
from routes.discord.api_connector import insertState, testState
from utils.jws import generateJWS
from models.user import UserModel
from utils.utils import postJson
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
    
    @postJson
    def post(self, data):
        if("code" not in data or "state" not in data or "redirect_uri" not in data):
            return {"state": 1, "msg": "Missing something in request."}, 401
        if(testState(data["state"]) == False):
            return {"state": 1, "msg": "Invalid state."}, 401

        if("name" not in data):
            data["name"] = ''
        if("surname" not in data):
            data["surname"] = ''
        if("adult" not in data):
            data["adult"] = ''
        if("school_id" not in data):
            data["school_id"] = ''

        user = UserModel.getByCode(data["code"], data["redirect_uri"], data["name"], data["surname"], data["adult"], data["school_id"])

        claims = {}
        claims[discord["userid_claim"]] = user.userId
        jws = generateJWS(claims)
        
        return {"jws":jws}