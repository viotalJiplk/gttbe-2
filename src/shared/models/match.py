from ..utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from ..utils.objectDbSync import ObjectDbSync
from ..utils.logging import defaultLogger
from .stage import StageModel

class MatchModel (ObjectDbSync):
    tableName = "matches"
    tableId = "matchId"
    def __init__(self, matchId:int=None, stageId:int=None, firstTeamId:int=None, secondTeamId:int=None, firstTeamResult:int=None, secondTeamResult:int=None):
        self.matchId = matchId
        self.stageId = stageId
        self.firstTeamId = firstTeamId
        self.secondTeamId = secondTeamId
        self.firstTeamResult = firstTeamResult
        self.secondTeamResult = secondTeamResult
        super().__init__()

    def toDict(self):
        return {
            "matchId": self.matchId,
            "stageId": self.stageId,
            "firstTeamId": self.firstTeamId,
            "secondTeamId": self.secondTeamId,
            "firstTeamResult": self.firstTeamResult,
            "secondTeamResult": self.secondTeamResult,
        }

    def __str__(self):
        return dumps(self.toDict())

    def getStage(self):
        return StageModel.getById(self.stageId)

    def getEvent(self):
        stage = self.getStage()
        if stage is None:
            defaultLogger.error("Inconsistent db")
            return None
        return stage.getEvent()

    @dbConn()
    def delete(self, cursor, db):
        query = "DELETE FROM `matches` WHERE `matchId` = %s"
        cursor.execute(query, (self.matchId,))

    @classmethod
    @dbConn()
    def create(cls, stageId:int, firstTeamId:int, secondTeamId:int, firstTeamResult:int, secondTeamResult:int, cursor, db):
        query = "INSERT INTO matches (stageId, firstTeamId, secondTeamId, firstTeamResult, secondTeamResult) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (stageId, firstTeamId, secondTeamId, firstTeamResult, secondTeamResult))
        return cls(matchId=cursor.lastrowid , stageId=stageId, firstTeamId = firstTeamId, secondTeamId = secondTeamId, firstTeamResult = firstTeamResult, secondTeamResult = secondTeamResult)
