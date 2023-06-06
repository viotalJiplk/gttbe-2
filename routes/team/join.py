from flask_restful import Resource, request

from models.team import TeamModel
from utils.jws import authorize

class Join(Resource):
    def post(self, joinString):
        try:
            auth_result = authorize(request)
            data = request.get_json()
        except:
            return {"state": 1, "msg": "This is jws protected json endpoint."}, 401
        if("nick" not in data or "rank" not in data or "max_rank" not in data or "role" not in data):
            return {"state": 1, "msg": "Missing nick, rank, max_rank or role."}, 401
        team = TeamModel.getByJoinString(joinString)
        team.join(userId=auth_result["userId"], nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"], role=data["role"])
        return {"teamId":team.teamId}, 200