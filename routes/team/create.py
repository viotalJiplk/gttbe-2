from flask_restful import Resource, request
from models.team import TeamModel
from utils.jws import jwsProtected
from utils.utils import postJson

class createTeam(Resource):

    @jwsProtected()
    @postJson
    def post(self, data, authResult):
        if("game_id" not in data or "name" not in data):
            return {"state": 1, "msg": "Missing game_id or name."}, 401
        if("nick" not in data or "rank" not in data or "max_rank" not in data):
            return {"state": 1, "msg": "Missing nick, rank, or max_rank of capitain."}, 401
        team = TeamModel(name=data["name"], gameId=data["game_id"], userId=authResult["userId"], nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"])
        return {"teamId": team.teamId}, 200