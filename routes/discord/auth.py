from flask_restful import Resource, request
from flask import redirect
from routes.discord.constants import *
import requests
from utils.errorlog import weberrorlog
from config import discord, selfref
from utils.db import getConnection
from routes.discord.api_connector import getuserobject, insertTokens, insertState, testState
from routes.discord.jws import generateJWS


class Auth(Resource):
    scopes = ["identify"]
    def get(self):
        state = insertState()
        if type(state) is dict:
            return weberrorlog(state["msg"], 500)
        return redirect(endpoint_url(state, "none"), 307)
        #could technicaly throw error if state is not unique
class Redirected(Resource):
    def get(self):
        code = request.args.get('code', default = '', type = str)
        state = request.args.get('state', default = '', type = str)
        if(code == '' or state == ''):
            return {"state": 1, "msg": "Missing code or state."}, 401
        if(testState(state) == False):
            return {"state": 1, "msg": "Invalid state."}, 401
        data = {
            'client_id': discord["client_id"],
            'client_secret': discord["client_secret"],
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': discord["redir_url"]
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            r = requests.post('%s/oauth2/token' % discord['api_endpoint'], data=data, headers=headers)
        except Exception as e:
            return weberrorlog("discord token endpoint error: "  + e.args[0], 401)
            #discord token endpoint error
        if(r.status_code != 200):
            return weberrorlog("discord token endpoint responded: " + str(r.status_code) + r.text, 401)
            #discord token endpoint error
        r = r.json()
        if(r["token_type"] != "Bearer"):
            return weberrorlog("discord token endpoint response  unknown token type", 401)
        if(r["access_token"] == ""):
            return weberrorlog("discord token endpoint response  missing access_token", 401)
        if(r["refresh_token"] == ""):
            return weberrorlog("discord token endpoint response  missing refresh_token", 401)
        
        user = getuserobject(r["access_token"])
        if 'state' in user.keys():
            if(user["state"] == 1):
                return weberrorlog(user["msg"], 500)
        insertTok = insertTokens(r, user["user"]["id"])
        if(insertTok != 200):
             return weberrorlog(insertTok["msg"], 500)
        claims = {}
        claims[selfref["root_url"] + "/discord/userid"] = user["user"]["id"]
        jws = generateJWS(claims)
        
        return {"jws":jws, "userobject": user}