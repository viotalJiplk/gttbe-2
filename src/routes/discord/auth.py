from flask_restful import Resource, request
from models.state import StateModel
from config import discord
from config import selfref
from utils.jws import generateJWS
from models.user import UserModel
from utils.utils import postJson
import urllib
import json

class Auth(Resource):
    def __endpoint_url(self, state, prompt="consent"):
        scope = "identify"
        state = urllib.parse.quote(state, safe='')
        # redir_url_urlencoded = urllib.parse.quote(discord["redir_url"], safe='')
        return "https://discord.com/oauth2/authorize?response_type=code&client_id="+str(discord["client_id"])+"&scope="+ scope +"&state="+ state +"&prompt=" + prompt

    def get(self):
        state = StateModel.create()
        return {"redirect_url": self.__endpoint_url(state.state, "none")}, 200
        # could technicaly throw error if state is not unique


class TokenEndpoint(Resource):

    @postJson
    def post(self, data):
        if("code" not in data or "state" not in data or "redirect_uri" not in data):
            return {"state": 1, "msg": "Missing something in request."}, 401
        if(StateModel.testAndDelete(data["state"]) == False):
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
        claims[discord["userid_claim"]] = user[0].userId
        jws = generateJWS(claims)

        return {"jws":jws, "userObject": user[1]}
