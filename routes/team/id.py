from flask_restful import Resource, request

from models.team import TeamModel
from utils.jws import authorize

class Team(Resource):
    def get(self, teamId):
        try:
            team = TeamModel.getById(teamId)
        except:
            return {"state": 1, "msg": "Wrong teamId."}, 401
        return {
            "teamId": team.teamId,
            "gameId": team.gameId,
            "Players": team.getPlayers()
        }, 200

class TeamJoinstring(Resource):
    def get(self, teamId):
        try:
            team = TeamModel.getById(teamId)
        except:
            return {"state": 1, "msg": "Wrong teamId."}, 401
        try:
            auth_result = authorize(request)
        except:
            return {"state": 1, "msg": "This is jws protected json endpoint."}, 401
        if(team.getUsersRole(auth_result["userId"]) != "Captain"):
            return {"state": 1, "msg": "You are not Captain of this team."}, 401
        return {"joinString": team.generateJoinString()}, 200

class Join(Resource):
    def post(self, teamId, joinString):
        try:
            auth_result = authorize(request)
            data = request.get_json()
        except:
            return {"state": 1, "msg": "This is jws protected json endpoint."}, 401
        if("nick" not in data or "rank" not in data or "max_rank" not in data or "role" not in data):
            return {"state": 1, "msg": "Missing nick, rank, max_rank or role."}, 400
        try:
            team = TeamModel.getById(teamId)
        except:
            return {"state": 1, "msg": "Wrong teamId."}, 401
        if(team.joinString != joinString):
            return {"state": 1, "msg": "Wrong joinString."}, 401
        try:
            team.join(userId=auth_result["userId"], nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"], role=data["role"])
        except:
            return {"state": 1, "msg": "Team full or you are in another team for this game."}, 401
        return {"teamId":team.teamId}, 200

class Kick(Resource):
    def delete(self, teamId, userId):
        try:
            auth_result = authorize(request)
        except:
            return {"state": 1, "msg": "This is jws protected json endpoint."}, 401
        try:
            team = TeamModel.getById(teamId)
        except:
            return {"state": 1, "msg": "Wrong teamId."}, 401
        try:
            if userId == "@me":
                team.leave(userId=auth_result["userId"])
            else:
                if(team.getUsersRole(auth_result["userId"]) == "Captain"):
                    team.leave(userId=userId)
                else:
                    return {"state": 1, "msg": "Cannot kick form team. You are not Captain of this team."}, 401
        except:
            return {"state": 1, "msg": "Cannot kick or leave team. Are you member of this team?"}, 401
        return {"teamId":team.teamId}, 200