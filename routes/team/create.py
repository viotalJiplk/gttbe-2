from flask_restful import Resource, request
from models.team import TeamModel
from utils.jws import verifyJWS

class createTeam(Resource):
    def post(self):
        try:
            data = request.get_json()
        except:
            return {"state": 1, "msg": "This is json endpoint."}, 401
        if(data["jws"] == '' or data["game_id"] == '' or data["name"] == ''):
            return {"state": 1, "msg": "Missing jws, game_id or name."}, 401
        try:
            trusted = verifyJWS(data["jws"])
        except:
            return {"state": 1, "msg": "Invalid jws."}, 401
        team = TeamModel(name=data["name"], gameId=data["game_id"])
        team.insert()