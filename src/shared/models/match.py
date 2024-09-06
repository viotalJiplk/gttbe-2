from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from ..utils import ObjectDbSync
from ..utils import defaultLogger
from .stage import StageModel, EventModel
from typing import Union

class MatchModel (ObjectDbSync):
    """Representation of match

    Attributes:
            matchId (int): id of match
            stageId (int): id of stage this match belongs to
            firstTeamId (int): id of first team of this match
            secondTeamId (int): id of second team of this match
            firstTeamResult (Union[int, None]): result of first team
            secondTeamResult (Union[int, None]): result of second team
    """
    tableName = "matches"
    tableId = "matchId"
    def __init__(self, matchId:int=None, stageId:int=None, firstTeamId:int=None, secondTeamId:int=None, firstTeamResult:Union[int, None]=None, secondTeamResult:Union[int, None]=None):
        """Initializes representation of match

        Args:
            matchId (int): id of match
            stageId (int): id of stage this match belongs to
            firstTeamId (int): id of first team of this match
            secondTeamId (int): id of second team of this match
            firstTeamResult (Union[int, None]): result of first team
            secondTeamResult (Union[int, None]): result of second team
        """
        self.matchId = matchId
        self.stageId = stageId
        self.firstTeamId = firstTeamId
        self.secondTeamId = secondTeamId
        self.firstTeamResult = firstTeamResult
        self.secondTeamResult = secondTeamResult
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
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
        """Returns stage of this match

        Returns:
            Union[None, StageModel]: stage of this match
        """
        return StageModel.getById(self.stageId)

    def getEvent(self):
        """Returns event of this match

        Returns:
            Union[None, EventModel]: event of this match
        """
        stage = self.getStage()
        if stage is None:
            defaultLogger.error("Inconsistent db")
            return None
        return stage.getEvent()

    @classmethod
    @dbConn()
    def create(cls, stageId:int, firstTeamId:int, secondTeamId:int, firstTeamResult: Union[int, None], secondTeamResult: Union[int, None], cursor, db):
        """Creates new match

        Args:
            stageId (int): id of stage this match belongs to
            firstTeamId (int): id of first team of this match
            secondTeamId (int): id of second team of this match
            firstTeamResult (Union[int, None]): result of first team
            secondTeamResult (Union[int, None]): result of second team
        Returns:
            MatchModel: new match
        """
        query = "INSERT INTO matches (stageId, firstTeamId, secondTeamId, firstTeamResult, secondTeamResult) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (stageId, firstTeamId, secondTeamId, firstTeamResult, secondTeamResult))
        return cls(matchId=cursor.lastrowid , stageId=stageId, firstTeamId = firstTeamId, secondTeamId = secondTeamId, firstTeamResult = firstTeamResult, secondTeamResult = secondTeamResult)
