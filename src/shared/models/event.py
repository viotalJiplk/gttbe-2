from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn, ObjectDbSync, fromTimeDelta
from json import dumps
from datetime import date, time
from mysql.connector.errors import IntegrityError
from typing import Union


class EventModel(ObjectDbSync):
    """Representation of event

    Attributes:
            eventId (Union[int, None]): id of event
            date (date): date of event
            beginTime (time): time when event starts
            endTime (time): time when event ends
            gameId (int): gameId of event
            description (str): description of event
            eventType (str): type of event
    """
    tableName="events"
    tableId="eventId"
    def __init__(self, eventId:int=None, date:date=date.fromisocalendar(1,1,1), beginTime:time=time(0,0,0,0), endTime:time=time(0,0,0,0), gameId:int=None, description:str="", eventType:str=None):
        """Initializes representation of event

        Args:
            eventId (Union[int, None]): id of event
            date (date): date of event
            beginTime (time): time when event starts
            endTime (time): time when event ends
            gameId (int): gameId of event
            description (str): description of event
            eventType (str): type of event
        """
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
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "eventId": self.eventId,
            "date": self.date.isoformat(),
            "beginTime": self.beginTime.strftime("%H:%M:%S"),
            "endTime": self.endTime.strftime("%H:%M:%S"),
            "gameId": self.gameId,
            "description": self.description,
            "eventType": self.eventType
        }

    @classmethod
    @dbConn()
    def create(cls, date: date, beginTime: time, endTime: time, gameId: int, description: str, eventType: str, cursor, db):
        """Creates representation of event

        Args:
            date (date): date of event
            beginTime (time): time when event starts
            endTime (time): time when event ends
            gameId (int): gameId of event
            description (str): description of event
            eventType (str): type of event
        """
        query = "INSERT INTO events (date, beginTime, endTime, gameId, description, eventType) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (date, beginTime, endTime, gameId, description, eventType))
        return cls(eventId=cursor.lastrowid, date=date, beginTime=beginTime, endTime=endTime, gameId=gameId, description=description, eventType= eventType)

    @classmethod
    @dbConn()
    def getById(cls, eventId, cursor, db):
        """Gets event representation by id

        Args:
            eventId (int): id of event

        Returns:
            EventModel: event representation
        """
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
        """Returns list of dict of all rows in db

            Returns:
                list[dict]: list dict of all rows (key = colum name)
        """
        rows = super().getAllDict()
        for index in range(0, len(rows)):
            rows[index]["date"] = rows[index]["date"].isoformat()
            rows[index]["beginTime"] = fromTimeDelta(rows[index]["beginTime"]).strftime("%H:%M")
            rows[index]["endTime"] = fromTimeDelta(rows[index]["endTime"]).strftime("%H:%M")
        return rows

    @dbConn()
    def listStages(self, cursor, db):
        """Lists all stages of this event

        Returns:
            list[dict]: stages list
        """
        query = "SELECT stageId, eventId, stageName, stageIndex FROM stages WHERE eventId = %s"
        cursor.execute(query, (self.eventId,))
        return fetchAllWithNames(cursor)

    @dbConn()
    def allMatchesDict(self, cursor, db):
        """Lists all matches of this event with details

        Returns:
            list[dict]: list of matches with details
        """
        query = "SELECT * FROM matchesAll WHERE eventId=%s"
        cursor.execute(query, (self.eventId,))
        rows = fetchAllWithNames(cursor)
        for index in range(0, len(rows)):
            rows[index]["date"] = rows[index]["date"].isoformat()
            rows[index]["beginTime"] = fromTimeDelta(rows[index]["beginTime"]).strftime("%H:%M:%S")
            rows[index]["endTime"] = fromTimeDelta(rows[index]["endTime"]).strftime("%H:%M:%S")
        return rows
