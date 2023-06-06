from utils.db import getConnection, fetchAllWithNames

class GameModel:
    def __init__(self, name=None, maxCaptains=None, maxMembers=None, maxReservists=None, gameId=None, dbsync=True):
        if(dbsync):
            db = getConnection(autocommit=False)
            cursor = db.cursor(buffered=True)
            try:
                query = "INSERT INTO games (name, maxCaptains, maxMembers, maxReservists) VALUES (%s, %s)"
                cursor.execute(query, (name, maxCaptains, maxMembers, maxReservists))
                cursor.execute("SELECT LAST_INSERT_ID();")
                row = cursor.fetchone()
                self.gameId = row[0]
                db.commit()
                cursor.close()
                db.close()
            except:
                db.rollback()
                cursor.close()
                db.close()
        else:
            self.gameId = gameId
        
        self.name = name
        self.maxCaptains = maxCaptains
        self.maxMembers = maxMembers
        self.maxReservists = maxReservists
    
    @classmethod
    def getById(self, gameId):
        db = getConnection(autocommit=True)
        cursor = db.cursor(buffered=True) 
        query = "SELECT name, maxCaptains, maxMembers, maxReservists, gameId FROM games WHERE gameId=%s"
        cursor.execute(query, (gameId,))
        row = cursor.fetchone()
        cursor.close()
        db.close()
        if(row):
            return GameModel(name=row[0], maxCaptains=row[1], maxMembers=row[2], maxReservists=row[3], gameId=row[4], dbsync=False)
        else:
            raise Exception("Game does not exist.")
    
    @classmethod
    def getAll(self):
        db = getConnection(autocommit=True)
        cursor = db.cursor(buffered=True) 
        query = "SELECT name, maxCaptains, maxMembers, maxReservists, gameId FROM games"
        cursor.execute(query)
        row = fetchAllWithNames(cursor)
        cursor.close()
        db.close()
        return row