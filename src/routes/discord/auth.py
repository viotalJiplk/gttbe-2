from flask_restx import Resource
from flask import Response
from shared.models import StateModel
from shared.utils import config, genState
from utils import generateJWS, returnParser, errorList, returnError, handleReturnableError, postJsonParse, postJson
from shared.models import UserModel
import urllib
import json
from datetime import datetime, timezone

discordUserObject = {
        "id": [str],
        "username": [str],
        "avatar": [str],
        "discriminator": [str],
        "public_flags": [int],
        "flags": [int],
        "banner": [str, type(None)],
        "accent_color": [int, type(None)],
        "global_name": [str, type(None)],
        "banner_color": [int, type(None)]
    }

class Auth(Resource):
    def __endpoint_url(self, state, prompt="consent"):
        scope = "identify"
        state = urllib.parse.quote(state, safe='')
        # redir_url_urlencoded = urllib.parse.quote(discord["redir_url"], safe='')
        return "https://discord.com/oauth2/authorize?response_type=code&client_id="+str(config.discord.client_id)+"&scope="+ scope +"&state="+ state +"&prompt=" + prompt
    @returnParser({
        "redirectUrl": [str]
    }, 200, False, False)
    def get(self):
        """
            Generates discord api uri.
            You should add &redirect_uri=$uri$ at the end so discord would redirect user to your client.
        Returns:
            dict: redirect url
        """
        state = StateModel.create()
        return {"redirectUrl": self.__endpoint_url(state.state, "none")}, 200
        # could technically throw error if state is not unique


class TokenEndpoint(Resource):
    @returnParser({
        "jws": [str],
        "userObject": discordUserObject
    })
    @returnError([errorList.auth.invalidState])
    @postJsonParse({
        "code": [str],
        "state": [str],
        "redirectUri": [str]
    })
    def post(self, data):
        """
            Exchange OAuth code for jws.
        Args:

        Returns:
            dict: jws and user info
        """
        if(StateModel.testAndDelete(data["state"]) == False):
            raise errorList.auth.invalidState

        if("name" not in data):
            data["name"] = None
        if("surname" not in data):
            data["surname"] = None
        if("adult" not in data):
            data["adult"] = None
        if("schoolId" not in data):
            data["schoolId"] = None

        user = UserModel.getByCode(data["code"], data["redirectUri"], data["name"], data["surname"], data["adult"], data["schoolId"])

        claims = {}
        claims[config.discord.userid_claim] = user[0].userId
        jws = generateJWS(claims, user[0].userId, ["backend"], datetime.now(timezone.utc), data["state"])

        return {"jws":jws, "userObject": user[1]}

class TestGetJWS(Resource):
    def get(self, userId):
        claims = {}
        claims[config.discord.userid_claim] = userId
        jws = generateJWS(claims, user[0].userId, ["backend"], datetime.now(timezone.utc), genState(20))

        return Response(f'Bearer {jws}', status=200, mimetype="text/plain")
