from ..utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date, time, timedelta
from ..utils.objectDbSync import ObjectDbSync

def fromTimeDelta(td: timedelta):
    totalSeconds = td.total_seconds()
    hours = int(totalSeconds // 3600)
    minutes = int((totalSeconds % 3600) // 60)
    seconds = int(totalSeconds % 60)
    return time(hour=hours, minute=minutes, second=seconds)


class EventModel(ObjectDbSync):
    tableName="events"
    tableId="eventId"
    def __init__(self, eventId:int=None, date:date=date.fromisocalendar(1,1,1), beginTime:time=time(0,0,0,0), endTime:time=time(0,0,0,0), gameId:int=None, description:str="", eventType:str=None):
        self.eventId = eventId
        self.date = date
        self.beginTime = beginTime
        self.endTime = endTime
        self.gameId = gameId
        self.description = description
        self.eventType = eventType
        super().__init__()

    def __str__(self):
        return dumps(self.toDict())

    def toDict(self):
        return {
            "eventId": self.eventId,
            "date": self.date.isoformat(),
            "beginTime": self.beginTime.strftime("%H:%M:%S"),
            "endTime": self.endTime.strftime("%H:%M:%S"),
            "gameId": self.gameId,
            "description": self.description,
            "eventType": self.eventType
        }

    @dbConn()
    def delete(self, cursor, db):
        query = "DELETE FROM events WHERE eventId = %s"
        cursor.execute(query, (self.eventId,))

    @classmethod
    @dbConn()
    def create(cls, date: date, beginTime: time, endTime: time, gameId: int, description: str, eventType: str, cursor, db):
        query = "INSERT INTO events (date, beginTime, endTime, gameId, description, eventType) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (date, beginTime, endTime, gameId, description, eventType))
        return cls(eventId=cursor.lastrowid, date=date, beginTime=beginTime, endTime=endTime, gameId=gameId, description=description, eventType= eventType)

    @classmethod
    @dbConn()
    def getById(cls, eventId, cursor, db):
        query = "SELECT eventId, date, beginTime, endTime, gameId, description, eventType FROM events WHERE eventId=%s"
        cursor.execute(query, (eventId,))
        row = fetchOneWithNames(cursor)
        if row:
            row["beginTime"] = fromTimeDelta(row["beginTime"])
            row["endTime"] = fromTimeDelta(row["endTime"])
            return cls(**row)
        else:
            return None

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        rows = super().getAllDict()
        for index in range(0, len(rows)):
            rows[index]["date"] = rows[index]["date"].isoformat()
            rows[index]["beginTime"] = fromTimeDelta(rows[index]["beginTime"]).strftime("%H:%M")
            rows[index]["endTime"] = fromTimeDelta(rows[index]["endTime"]).strftime("%H:%M")
        return rows

    @dbConn()
    def allMatchesDict(self, cursor, db):
        query = "SELECT * FROM matchesAll WHERE eventId=%s"
        cursor.execute(query, (self.eventId,))
        rows = fetchAllWithNames(cursor)
        for index in range(0, len(rows)):
            rows[index]["date"] = rows[index]["date"].isoformat()
            rows[index]["beginTime"] = fromTimeDelta(rows[index]["beginTime"]).strftime("%H:%M")
            rows[index]["endTime"] = fromTimeDelta(rows[index]["endTime"]).strftime("%H:%M")
        return rows
