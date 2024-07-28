from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date
from utils.objectDbSync import ObjectDbSync

class GameModel(ObjectDbSync):
    tableName = "games"
    tableId = "gameId"

    def __init__(self, name=None, registrationStart=date.fromisocalendar(1,1,1), registrationEnd=date.fromisocalendar(9999,1,1), maxCaptains=None, maxMembers=None, maxReservists=None, minCaptains=None, minMembers=None, minReservists=None, gameId=None, gamePage=None, maxTeams=None):
        self.gameId = gameId
        self.name = name
        self.registrationStart = registrationStart
        self.registrationEnd = registrationEnd
        self.maxCaptains = maxCaptains
        self.maxMembers = maxMembers
        self.maxReservists = maxReservists
        self.minCaptains = minCaptains
        self.minMembers = minMembers
        self.minReservists = minReservists
        self.gamePage = gamePage
        self.maxTeams = maxTeams

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
            "maxCaptains": self.maxCaptains,
            "maxMembers": self.maxMembers,
            "maxReservists": self.maxReservists,
            "minCaptains": self.minCaptains,
            "minMembers": self.minMembers,
            "minReservists": self.minReservists,
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

    @dbConn()
    def update(self, cursor, db):
        query = "UPDATE `games` SET registrationStart = %s, registrationEnd = %s, maxCaptains = %s, maxMembers = %s, maxReservists = %s, minCaptains = %s, minMembers = %s, minReservists = %s, gamePage = %s, maxTeams = %s WHERE gameId = %s"
        cursor.execute(query, (self.registrationStart, self.registrationEnd, self.maxCaptains, self.maxMembers, self.maxReservists, self.minCaptains, self.minMembers, self.minReservists, self.gamePage, self.gameId, self.maxTeams))
        return True

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        rows = super().getAllDict()
        for index in range(0, len(rows)):
            rows[index]["registrationStart"] = rows[index]["registrationStart"].isoformat()
            rows[index]["registrationEnd"] = rows[index]["registrationEnd"].isoformat()
        return rows
