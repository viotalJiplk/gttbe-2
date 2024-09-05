from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn, ObjectDbSync, fromTimeDelta
from json import dumps
from .event import EventModel

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
    def allMatchesDict(self, cursor, db):
        query = "SELECT * FROM matchesAll WHERE stageId=%s"
        cursor.execute(query, (self.stageId,))
        rows = fetchAllWithNames(cursor)
        for index in range(0, len(rows)):
            rows[index]["date"] = rows[index]["date"].isoformat()
            rows[index]["beginTime"] = fromTimeDelta(rows[index]["beginTime"]).strftime("%H:%M")
            rows[index]["endTime"] = fromTimeDelta(rows[index]["endTime"]).strftime("%H:%M")
        return rows

    @classmethod
    @dbConn()
    def create(cls, eventId:int, stageName:str, stageIndex:int, cursor, db):
        query = "INSERT INTO stages (eventId, stageName, stageIndex) VALUES (%s, %s, %s)"
        cursor.execute(query, (eventId, stageName, stageIndex))
        return cls(stageId=cursor.lastrowid, eventId=eventId, stageName=stageName, stageIndex=stageIndex)
