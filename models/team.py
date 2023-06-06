from utils.db import getConnection, fetchAllWithNames
from models.game import GameModel
from utils.generator import genState

class TeamModel:
    def __init__(self, name=None, gameId = None, userId=None, nick=None, rank=None, maxRank=None, joinString=None, teamId=None,  dbsync=True):
        if(dbsync): 
            db = getConnection(autocommit=False)
            cursor = db.cursor(buffered=True)
            try:
                query = "INSERT INTO teams (name, gameId) VALUES (%s, %s)"
                values = (name, gameId)
                cursor.execute(query, values)
                cursor.execute("SELECT LAST_INSERT_ID();")
                row = cursor.fetchone()
                query = "INSERT INTO registrations (userId, teamId, nick, role, rank, maxRank) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (userId, row[0], nick, "Captain", rank, maxRank)
                cursor.execute(query, values)                           
                cursor.execute("SELECT LAST_INSERT_ID();")
                row = cursor.fetchone()
                db.commit()
                cursor.close()
                db.close()
                self.teamId = row[0]
            except:
                db.rollback()
                cursor.close()
                db.close()
                raise Exception("Cannot create team!")
        else:
            self.teamId = teamId

        self.name = name
        self.gameId = gameId
        self.joinString = joinString

    @classmethod
    def getById(cls, teamId):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        query = "SELECT name, gameId, joinString,teamId FROM teams WHERE teamId=%s"
        cursor.execute(query, (teamId,))
        row = cursor.fetchone()
        cursor.close()
        db.close()
        if not row:
            cursor.close()
            db.close()
            raise Exception("Team does not exist.")
        return TeamModel(name=row[0], gameId=row[1], joinString=row[2], teamId=row[3], dbsync=False)
    
    @classmethod
    def getByName(cls, name):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        query = "SELECT name, gameId, joinString, teamId FROM teams WHERE name=%s"
        cursor.execute(query, (name))
        row = cursor.fetchone()
        cursor.close()
        db.close()
        if not row:
            cursor.close()
            db.close()
            raise Exception("Team does not exist.")
        return TeamModel(name=row[0], gameId=row[1], joinString=row[2], teamId=row[3], dbsync=False)

    def join(self, userId, nick, rank, maxRank, role):
        db = getConnection(autocommit=False)
        cursor = db.cursor(buffered=True)
        game = self.getGame()
        try:
            query = "INSERT INTO registrations (userId, teamId, nick, role, rank, maxRank) VALUES (%(userId)s, %(teamId)s, %(nick)s, %(role)s, %(rank)s, %(maxRank)s)"
            values = {"userId": userId, "teamId": self.teamId, "nick": nick, "role": role, "rank": rank, "maxRank": maxRank}
            cursor.execute(query, values)
            query = "SELECT COUNT(*) FROM registrations WHERE teamId=%(teamId)s and role=%(role)s"
            values = {"teamId":self.teamId,"role":role}
            cursor.execute(query, values)
            row = cursor.fetchone()
            if(row[0] > getattr(game, "max"+role+"s")):
                db.rollback()
                raise Exception("Role is full.")
            else:
                db.commit()
                cursor.close()
                db.close()
        except:
            cursor.close()
            db.close()
            raise Exception("Cannot join team.")
    
    def leave(self, userId):
        db = getConnection(autocommit=True)
        cursor = db.cursor(buffered=False)
        try:
            query = "DELETE FROM `registrations` WHERE `userId` = %(userId)s AND `teamId` = %(teamId)s LIMIT 1"
            values = {"userId":userId, "teamId":self.teamId}
            query_return = cursor.execute(query, values)
            cursor.close()
            db.close()
        except:
            cursor.close()
            db.close()
            raise Exception("Cannot leave team.")

    def getGame(self):
        return GameModel.getById(self.gameId)
    
    def getPlayers(self):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        query = "SELECT `userid`, `nick`, `role`  FROM `registrations` WHERE teamId=%(teamId)s ORDER BY `role` ASC"
        cursor.execute(query, {"teamId": self.teamId})
        result = fetchAllWithNames(cursor)
        cursor.close()
        db.close()
        if not result:
            raise Exception("Team does not exist.")
        return result
    
    def generateJoinString(self):
        joinString = genState(200)
        db = getConnection()
        cursor = db.cursor(buffered=True)
        try:
            query = "UPDATE `teams` SET `joinString` = %(joinString)s WHERE `teamId` = %(teamId)s;"
            cursor.execute(query, {"joinString":  joinString, "teamId": self.teamId})
            self.joinString = joinString
            return joinString
        except:
            raise Exception("Team does not exist.")
    
    def getUsersRole(self, userId):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        query = 'SELECT role FROM `registrations` WHERE `teamId`=%(teamId)s AND `userId`=%(userId)s'
        cursor.execute(query, {"teamId": self.teamId, "userId": userId})
        result = fetchAllWithNames(cursor)
        cursor.close()
        db.close()
        if(result):
            return result[0]["role"]
        else:
            return False