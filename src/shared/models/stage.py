from ..utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from .event import EventModel
from ..utils.objectDbSync import ObjectDbSync

class StageModel(ObjectDbSync):
    tableName = "stages"
    tableId = "stageId"
    def __init__(self, stageId:int=None, eventId:int=None, stageName:str="", stageIndex:int=None):
        self.stageId = stageId
        self.eventId = eventId
        self.stageName = stageName
        self.stageIndex = stageIndex
        super().__init__()

    def toDict(self):
        return {
            "stageId": self.stageId,
            "eventId": self.eventId,
            "stageName": self.stageName,
            "stageIndex": self.stageIndex,
        }

    def __str__(self):
        return dumps(self.toDict())

    def getEvent(self):
        return EventModel.getById(self.eventId)

    @dbConn()
    def delete(self, cursor, db):
        query = "DELETE FROM `stages` WHERE `stageId` = %s"
        cursor.execute(query, (self.stageId,))

    @classmethod
    @dbConn()
    def create(cls, eventId:int, stageName:str, stageIndex:int, cursor, db):
        query = "INSERT INTO stages (eventId, stageName, stageIndex) VALUES (%s, %s, %s)"
        cursor.execute(query, (eventId, stageName, stageIndex))
        return cls(stageId=cursor.lastrowid, eventId=eventId, stageName=stageName, stageIndex=stageIndex)
