from flask_restful import Resource
from models.stage import StageModel
from utils.role import getRole
from utils.jws import jwsProtected
from utils.utils import postJsonParse
from datetime import datetime
from models.role import RoleModel
from models.event import EventModel
from models.match import MatchModel

class Matches(Resource):
    def get(self, matchId):
        match = MatchModel.getById(matchId=matchId)
        if match is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        return match.toDict()
   
    @jwsProtected()
    def delete(self, authResult, matchId):
        match = MatchModel.getById(matchId=matchId)
        if match is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        stage = StageModel.getById(match.stageId)
        if stage is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        event = EventModel.getById(stage.eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        try:
            match.delete()
        except e:
            return {"kind": "DATA", "msg": "There are still data, that is dependent on this."}, 401
        return

class MatchCreate(Resource):
    @jwsProtected()
    @postJsonParse(expectedJson={
        "stageId": [int],
        "firstTeamId": [int],
        "secondTeamId": [int],
        "firstTeamResult": [int],
        "secondTeamResult": [int],
    })
    def post(self, data, authResult):
        stage = StageModel.getById(stageId=data["stageId"])
        if stage is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        event = EventModel.getById(stage.eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        return MatchModel.create(data["stageId"], data["firstTeamId"], data["secondTeamId"], data["firstTeamResult"], data["secondTeamId"]).toDict()