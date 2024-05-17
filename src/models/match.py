from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps

class MatchModel:
    table = "matches"
    def __init__(self, matchId:int=None, stageId:int=None, firstTeamId:int=None, secondTeamId:int=None, firstTeamResult:int=None, secondTeamId:int=None):        
        self.matchId = matchId
        self.stageId = stageId
        self.firstTeamId = firstTeamId
        self.secondTeamId = secondTeamId
        self.firstTeamResult = firstTeamResult
        self.secondTeamResult = secondTeamResult

    def toDict(self):
        return {
            "eventId": self.eventId,
            "stageId": self.stageId,
            "firstTeamId": self.firstTeamId,
            "secondTeamId": self.secondTeamId,
            "firstTeamResult": self.firstTeamResult,
            "secondTeamResult": self.secondTeamResult,
        }

    def __str__(self):
        return dumps(self.toDict())
    
    @dbConn()
    def delete(self, cursor, db):
        query = "DELETE FROM `matches` WHERE `matchId` = %s"
        cursor.execute(query, (self.matchId,))
    
    @classmethod
    @dbConn()
    def create(cls, stageId:int, firstTeamId:int, secondTeamId:int, firstTeamResult:int, secondTeamId:int, cursor, db):
        query = "INSERT INTO matches (stageId, eventId, firstTeamId, secondTeamId, firstTeamResult, secondTeamId) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (stageId, firstTeamId, secondTeamId, firstTeamResult, secondTeamId))
        return cls(matchId=cursor.lastrowid , stageId=stageId, eventId=eventId, stageName=stageName, stageIndex=stageIndex)

    @classmethod
    @dbConn()
    def getById(cls, matchId, cursor, db):
        query = "SELECT matchId, stageId, eventId, firstTeamId, secondTeamId, firstTeamResult, secondTeamId FROM matches WHERE matchId=%s"
        cursor.execute(query, (matchId,))
        row = fetchOneWithNames(cursor)
        if row:
            return cls(**row)
        else:
            return None

    @classmethod
    @dbConn()
    def getAll(cls, cursor, db):
        query = "SELECT matchId, stageId, eventId, firstTeamId, secondTeamId, firstTeamResult, secondTeamId FROM matches"
        cursor.execute(query)
        rows = fetchAllWithNames(cursor)
        result = []
        for row in rows:
            result.append(cls(**row))
        return result