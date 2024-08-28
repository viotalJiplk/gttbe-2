from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date
from ..utils import ObjectDbSync

class GameModel(ObjectDbSync):
    tableName = "games"
    tableId = "gameId"

    def __init__(self, name=None, registrationStart=date.fromisocalendar(1,1,1), registrationEnd=date.fromisocalendar(9999,1,1), maxCaptains=None, maxMembers=None, maxReservists=None, minCaptains=None, minMembers=None, minReservists=None, gameId=None, gamePage=None, maxTeams=None):
        self.gameId = gameId
        self.name = name
        self.registrationStart = registrationStart
        self.registrationEnd = registrationEnd
        self.gamePage = gamePage
        self.maxTeams = maxTeams
        super().__init__()

    def canBeRegistered(self):
        # <registrationStart, registrationEnd)
        return (date.today() >= self.registrationStart) & (date.today() < self.registrationEnd)

    def getGamePage(self):
        return self.gamePage

    def toDict(self):
        return {
            "gameId": self.gameId,
            "name": self.name,
            "registrationStart": self.registrationStart.isoformat(),
            "registrationEnd": self.registrationEnd.isoformat(),
            "maxTeams": self.maxTeams
        }

    def __str__(self):
        return dumps(self.toDict())

    @classmethod
    @dbConn()
    def create(cls, name: str, registrationStart: date, registrationEnd: date, maxCaptains: int, maxMembers: int, maxReservists: int, cursor, db):
        query = "INSERT INTO games (name, maxCaptains, maxMembers, maxReservists, maxTeams) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, maxCaptains, maxMembers, maxReservists))
        return cls(gameId=cursor.lastrowid, name=name, maxCaptains=maxCaptains, maxMembers=maxMembers, maxReservists=maxReservists)

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        rows = super().getAllDict()
        for index in range(0, len(rows)):
            rows[index]["registrationStart"] = rows[index]["registrationStart"].isoformat()
            rows[index]["registrationEnd"] = rows[index]["registrationEnd"].isoformat()
        return rows
