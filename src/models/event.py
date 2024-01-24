from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date, time, timedelta

def fromTimeDelta(td: timedelta):
    def format(string):
        if len(string) < 2:
            return  "0" + string
        else:
            return string
    hours = str(int(td.seconds/3600))
    minutes = format(str(int((td.seconds/60)%60)))
    return hours + ":" + minutes

class EventModel:
    def __init__(self, eventId=None, date=date.fromisocalendar(1,1,1), beginTime=time(0,0,0,0), endTime=time(0,0,0,0), gameId=None, description=""):        
        self.eventId = eventId
        self.date = date
        self.beginTime = beginTime
        self.endTime = endTime
        self.gameId = gameId
        self.description = description

    def __str__(self):
        return dumps({
            "eventId": self.eventId,
            "date": self.date,
            "beginTime": fromTimeDelta(self.beginTime),
            "endTime": fromTimeDelta(self.endTime.hour()),
            "gameId": self.gameId,
            "description": self.description,
        })

    @classmethod
    @dbConn()
    def create(cls, date: date, beginTime: time, endTime: time, gameId: int, description: str, cursor, db):
        query = "INSERT INTO events (date, beginTime, endTime, gameId, description) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (date, beginTime, endTime, gameId, description))
        return cls(date=date, beginTime=beginTime, endTime=endTime, gameId=gameId, description=description)
    
    @classmethod
    @dbConn()
    def getById(cls, eventId, cursor, db):
        query = "SELECT eventId, date, beginTime, endTime, gameId, description FROM events WHERE eventId=%s"
        cursor.execute(query, (eventId,))
        row = fetchOneWithNames(cursor)
        if row:
            return cls(**row)
        else:
            return None
    
    @classmethod
    @dbConn()
    def getAll(cls, cursor, db):
        query = "SELECT eventId, date, beginTime, endTime, gameId, description FROM events"
        cursor.execute(query)
        rows = fetchAllWithNames(cursor)
        result = []
        for row in rows:
            result.append(cls(**row))
        return result

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        query = "SELECT eventId, date, beginTime, endTime, gameId, description FROM events"
        cursor.execute(query)
        rows = fetchAllWithNames(cursor)
        result = []
        for index in range(0, len(rows)):
            rows[index]["date"] = rows[index]["date"].isoformat()
            rows[index]["beginTime"] = fromTimeDelta(rows[index]["beginTime"])
            rows[index]["endTime"] = fromTimeDelta(rows[index]["endTime"])
        return rows