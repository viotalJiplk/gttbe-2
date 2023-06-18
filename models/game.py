from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn

class GameModel:
    def __init__(self, name=None, maxCaptains=None, maxMembers=None, maxReservists=None, gameId=None):        
        self.gameId = gameId
        self.name = name
        self.maxCaptains = maxCaptains
        self.maxMembers = maxMembers
        self.maxReservists = maxReservists

    @classmethod
    @dbConn()
    def create(cls, name: str, maxCaptains: int, maxMembers: int, maxReservists: int):
        query = "INSERT INTO games (name, maxCaptains, maxMembers, maxReservists) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, maxCaptains, maxMembers, maxReservists))
        return cls(name=name, maxCaptains=maxCaptains, maxMembers=maxMembers, maxReservists=maxReservists)
    
    @classmethod
    @dbConn()
    def getById(cls, gameId, cursor, db):
        query = "SELECT gameId, name, maxCaptains, maxMembers, maxReservists, gameId FROM games WHERE gameId=%s"
        cursor.execute(query, (gameId,))
        row = fetchOneWithNames(cursor)
        if row:
            return cls(**row)
        else:
            return None
    
    @classmethod
    @dbConn()
    def getAll(cls, cursor, db):
        query = "SELECT name, maxCaptains, maxMembers, maxReservists, gameId FROM games"
        cursor.execute(query)
        row = fetchAllWithNames(cursor)
        return row