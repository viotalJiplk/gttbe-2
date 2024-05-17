from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps

class StageModel:
    def __init__(self, stageId:int=None, stageIndex:int=None, stageName:str="", stageIndex:int=None):        
        self.stageId = stageId
        self.eventId = eventId
        self.stageName = stageName
        self.stageIndex = stageIndex

    def toDict():
        return {
            "stageId": self.stageId,
            "eventId": self.eventId,
            "stageName": self.stageName,
            "stageIndex": self.stageIndex,
        }

    def __str__(self):
        return dumps(self.toDict())
    
    @dbConn()
    def delete(self, cursor, db):
        query = "DELETE FROM `stages` WHERE `stageId` = %s"
        cursor.execute(query, (self.stageId,))
    
    @classmethod
    @dbConn()
    def create(cls, stageIndex:int, stageName:str, stageIndex:int, cursor, db):
        query = "INSERT INTO stages (eventId, stageName, stageIndex) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (eventId, stageName, stageIndex))
        return cls(stageId=cursor.lastrowid, eventId=eventId, stageName=stageName, stageIndex=stageIndex)

    @classmethod
    @dbConn()
    def getById(cls, stageId, cursor, db):
        query = "SELECT stageId, eventId, stageName, stageIndex FROM stages WHERE stageId=%s"
        cursor.execute(query, (eventId,))
        row = fetchOneWithNames(cursor)
        if row:
            return cls(**row)
        else:
            return None

    @classmethod
    @dbConn()
    def getAll(cls, cursor, db):
        query = "SELECT stageId, eventId, stageName, stageIndex FROM stages"
        cursor.execute(query)
        rows = fetchAllWithNames(cursor)
        result = []
        for row in rows:
            result.append(cls(**row))
        return result