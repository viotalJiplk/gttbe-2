from flask_restful import Resource, request

from models.team import TeamModel
from utils.jws import jwsProtected
from functools import wraps
from utils.utils import postJson
from utils.errorlog import weberrorlog
from models.user import UserModel

def getTeam(func):
    
    @wraps(func)
    def wrapGetTeam(*args, **kwargs):
        team = TeamModel.getById(kwargs['teamId'])
        if team is None:
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
        if team.getUsersRole(authResult["userId"]) != "Captain":
            return {"kind": "TEAMROLE", "msg": "You are not Captain of this team."}, 401
        joinString = team.generateJoinString()
        if joinString is None:
            return {"state": "TEAM", "msg": "Team does not exist"}, 401
        return {"joinString": team.generateJoinString()}, 200


class Join(Resource):
    
    @jwsProtected()
    @getTeam
    @postJson
    def post(self, authResult, team, data, teamId, joinString):
        if("nick" not in data or "rank" not in data or "max_rank" not in data or "role" not in data):
            return {"kind": "PAYLOAD", "msg": "Missing nick, rank, max_rank or role."}, 400
        if(team.joinString != joinString):
            return {"kind": "JOIN", "msg": "Wrong joinString."}, 401
        user = UserModel.getById(authResult["userId"])
        if user is None:
            return {"kind": "JOIN", "msg": "User is not in database."}, 404
        if not user.canRegister():
            return {"kind": "JOIN", "msg": "You havent filled info required for creating Team."}, 404
        if not team.join(userId=authResult["userId"], nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"], role=data["role"]):
            return {"kind": "JOIN", "msg": "Team full or you are in another team for this game."}, 401
        return {"teamId":team.teamId}, 200


class Kick(Resource):
    
    @jwsProtected()
    @getTeam
    def delete(self, authResult, team, teamId, userId):
        try:
            if userId == "@me":
                if not team.leave(userId=authResult["userId"]):
                    return {"kind": "TEAM", "msg": "Cannot kick form team. You are not part of this team."}, 404

            else:
                if(team.getUsersRole(authResult["userId"]) == "Captain"):
                    if not team.leave(userId=userId):
                        return {"kind": "TEAM", "msg": "Cannot kick form team. User is not part of this team."}, 404
                else:
                    return {"kind": "TEAMROLE", "msg": "Cannot kick form team. You are not Captain of this team."}, 401
        except:
            return {"kind": "TEAMROLE", "msg": "Cannot kick or leave team. Are you member of this team?"}, 401
        return {"teamId":team.teamId}, 200