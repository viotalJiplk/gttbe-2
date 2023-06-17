from flask_restful import Resource, request

from models.team import TeamModel
from utils.jws import jwsProtected
from functools import wraps
from utils.utils import postJson

def getTeam(func):
    
    @wraps(func)
    def wrapGetTeam(*args, **kwargs):
        try:
            team = TeamModel.getById(kwargs['teamId'])
        except:
            return {"kind": "TEAM", "msg": "Wrong teamId."}, 401
        return func(team=team, *args, **kwargs)
    return wrapGetTeam


class Team(Resource):

    @getTeam
    def get(self, team, teamId):
        return {
            "teamId": team.teamId,
            "gameId": team.gameId,
            "Players": team.getPlayers()
        }, 200


class TeamJoinstring(Resource):
    
    @jwsProtected()
    @getTeam
    def get(self, authResult, team, teamId):
        if(team.getUsersRole(authResult["userId"]) != "Captain"):
            return {"state": 1, "msg": "You are not Captain of this team."}, 401
        return {"joinString": team.generateJoinString()}, 200


class Join(Resource):
    
    @jwsProtected()
    @getTeam
    @postJson
    def post(self, authResult, team, data, teamId, joinString):
        if("nick" not in data or "rank" not in data or "max_rank" not in data or "role" not in data):
            return {"state": 1, "msg": "Missing nick, rank, max_rank or role."}, 400
        if(team.joinString != joinString):
            return {"state": 1, "msg": "Wrong joinString."}, 401
        try:
            team.join(userId=authResult["userId"], nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"], role=data["role"])
        except:
            return {"state": 1, "msg": "Team full or you are in another team for this game."}, 401
        return {"teamId":team.teamId}, 200


class Kick(Resource):
    
    @jwsProtected()
    @getTeam
    def delete(self, authResult, team, teamId, userId):
        try:
            if userId == "@me":
                team.leave(userId=authResult["userId"])
            else:
                if(team.getUsersRole(authResult["userId"]) == "Captain"):
                    team.leave(userId=userId)
                else:
                    return {"state": 1, "msg": "Cannot kick form team. You are not Captain of this team."}, 401
        except:
            return {"state": 1, "msg": "Cannot kick or leave team. Are you member of this team?"}, 401
        return {"teamId":team.teamId}, 200