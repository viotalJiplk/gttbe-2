from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date

class GameModel:
    def __init__(self, name=None, registrationStart=date.fromisocalendar(1,1,1), registrationEnd=date.fromisocalendar(9999,1,1), maxCaptains=None, maxMembers=None, maxReservists=None, minCaptains=None, minMembers=None, minReservists=None, gameId=None, gamePage=None):        
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

    def canBeRegistered(self):
        # <registrationStart, registrationEnd)
        return (date.today() >= self.registrationStart) & (date.today() < self.registrationEnd)

    def getGamePage(self):
        return self.gamePage

    def __str__(self):
        return dumps({
            "gameId": self.gameId,
            "name": self.name,
            "registrationStart": self.registrationStart.isoformat(),
            "registrationEnd": self.registrationEnd.isoformat(),
            "maxCaptains": self.maxCaptains,
            "maxMembers": self.maxMembers,
            "maxReservists": self.maxReservists,
            "minCaptains": self.minCaptains,
            "minMembers": self.minMembers,
            "minReservists": self.minReservists
        })

    @classmethod
    @dbConn()
    def create(cls, name: str, maxCaptains: int, maxMembers: int, maxReservists: int):
        query = "INSERT INTO games (name, maxCaptains, maxMembers, maxReservists) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, maxCaptains, maxMembers, maxReservists))
        return cls(name=name, maxCaptains=maxCaptains, maxMembers=maxMembers, maxReservists=maxReservists)
    
    @classmethod
    @dbConn()
    def getById(cls, gameId, cursor, db):
        query = "SELECT gameId, name, registrationStart, registrationEnd, maxCaptains, maxMembers, maxReservists, minCaptains, minMembers, minReservists, gameId, gamePage FROM games WHERE gameId=%s"
        cursor.execute(query, (gameId,))
        row = fetchOneWithNames(cursor)
        if row:
            return cls(**row)
        else:
            return None
    
    @classmethod
    @dbConn()
    def getAll(cls, cursor, db):
        query = "SELECT name, registrationStart, registrationEnd, maxCaptains, maxMembers, maxReservists, minCaptains, minMembers, minReservists, gameId, gamePage FROM games"
        cursor.execute(query)
        rows = fetchAllWithNames(cursor)
        result = []
        for row in rows:
            result.append(cls(**row))
        return result

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        query = "SELECT name, registrationStart, registrationEnd, maxCaptains, maxMembers, maxReservists, minCaptains, minMembers, minReservists, gameId FROM games"
        cursor.execute(query)
        rows = fetchAllWithNames(cursor)
        result = []
        for index in range(0, len(rows)):
            rows[index]["registrationStart"] = rows[index]["registrationStart"].isoformat()
            rows[index]["registrationEnd"] = rows[index]["registrationEnd"].isoformat()
        return rows