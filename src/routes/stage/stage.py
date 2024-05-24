from flask_restful import Resource
from models.stage import StageModel
from utils.role import getRole
from utils.jws import jwsProtected
from utils.utils import postJsonParse, postJson
from datetime import datetime
from models.role import RoleModel
from models.event import EventModel

accessibleAttributes = {
    "eventId": [int],
    "stageName": [str],
    "stageIndex": [int],
}

class Stages(Resource):
    def get(self, stageId):
        stage = StageModel.getById(stageId=stageId)
        if stage is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        return stage.toDict()
   
    @jwsProtected()
    def delete(self, authResult, stageId):
        stage = StageModel.getById(stageId)
        if stage is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        event = EventModel.getById(stage.eventId)
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        try:
            stage.delete()
        except e:
            return {"kind": "DATA", "msg": "There are still data, that is dependent on this."}, 401
        return

    @jwsProtected()
    @postJson
    def put(self, data, authResult, stageId):
        stage = StageModel.getById(stageId=stageId)
        if stage is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        event = stage.getEvent()
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin", "gameOrganizer"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        for x in data:
            if x in accessibleAttributes:
                if type(data[x]) in accessibleAttributes[x]:
                    setattr(stage, x, data[x])
        return stage.toDict()

class StageCreate(Resource):
    @jwsProtected()
    @postJsonParse(expectedJson=accessibleAttributes)
    def post(self, data, authResult):
        event = EventModel.getById(eventId=data["eventId"])
        if event is None:
            return {"kind": "DATA", "msg": "Requested resource does not exist."}, 404
        if not RoleModel.hasRole(authResult["userId"], ["admin"], event.gameId):
            return {"kind": "ROLE", "msg": "Inadequate role."}, 401
        return StageModel.create(data["eventId"], data["stageName"], data["stageIndex"]).toDict()