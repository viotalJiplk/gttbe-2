from flask_restful import Resource, request
from models.team import TeamModel
from utils.jws import jwsProtected
from utils.utils import postJson
from models.user import UserModel

class createTeam(Resource):

    @jwsProtected()
    @postJson
    def post(self, data, authResult):
        if("game_id" not in data or "name" not in data):
            return {"state": 1, "msg": "Missing game_id or name."}, 403
        if("nick" not in data or "rank" not in data or "max_rank" not in data):
            return {"state": 1, "msg": "Missing nick, rank, or max_rank of capitain."}, 403
        user = UserModel.getById(authResult["userId"])
        if user is None:
            return {"kind": "JOIN", "msg": "User is not in database."}, 404
        if not user.canRegister():
            return {"kind": "JOIN", "msg": "You havent filled info required for creating Team."}, 404

        team = TeamModel.create(name=data["name"], gameId=data["game_id"], userId=authResult["userId"], nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"])
        
        if team is None:
            return {"kind": "JOIN", "msg": "Team full or you are in another team for this game."}, 403
        
        return {"teamId": team.teamId}, 200