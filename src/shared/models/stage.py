from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn, ObjectDbSync, fromTimeDelta
from json import dumps
from .event import EventModel
from typing import Union

class StageModel(ObjectDbSync):
    """Representation of stage

    Attributes:
            stageId (int): id of stage
            eventId (int): id of event this stage belongs to
            stageName (str): name of the stage
            stageIndex (int): index of the stage in event
    """
    tableName = "stages"
    tableId = "stageId"
    def __init__(self, stageId:int=None, eventId:int=None, stageName:str="", stageIndex:int=None):
        """Initializes representation of stage

        Args:
            stageId (int): id of stage
            eventId (int): id of event this stage belongs to
            stageName (str): name of the stage
            stageIndex (int): index of the stage in event
        """
        self.stageId = stageId
        self.eventId = eventId
        self.stageName = stageName
        self.stageIndex = stageIndex
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "stageId": self.stageId,
            "eventId": self.eventId,
            "stageName": self.stageName,
            "stageIndex": self.stageIndex,
        }

    def __str__(self):
        return dumps(self.toDict())

    def getEvent(self):
        """Returns event of this stage

        Returns:
            Union[None, EventModel]: event of this match
        """
        return EventModel.getById(self.eventId)

    @dbConn()
    def allMatchesDict(self, cursor, db):
        """Lists all matches of this stage with details

        Returns:
            list[dict]: list of matches with details
        """
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
        """Creates new stage

        Args:
            eventId (int): id of event this stage belongs to
            stageName (str): name of the stage
            stageIndex (int): index of the stage in event
        Returns:
            StageModel: new stage
        """
        query = "INSERT INTO stages (eventId, stageName, stageIndex) VALUES (%s, %s, %s)"
        cursor.execute(query, (eventId, stageName, stageIndex))
        return cls(stageId=cursor.lastrowid, eventId=eventId, stageName=stageName, stageIndex=stageIndex)
