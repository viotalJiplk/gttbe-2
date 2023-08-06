from utils.db import getConnection, fetchAllWithNames, fetchOneWithNames, dbConn
from models.game import GameModel
from utils.generator import genState
from mysql.connector import IntegrityError

class TeamModel:
    def __init__(self, name, gameId, teamId, joinString=None):
        self.name = name
        self.gameId = gameId
        self.teamId = teamId
        self.joinString = joinString

    @classmethod
    @dbConn(autocommit=False, buffered=True)
    def create(cls, name, gameId, userId, nick, rank, maxRank, cursor, db):
        try:
            query = "INSERT INTO teams (name, gameId) VALUES (%s, %s)"
            values = (name, gameId)
            cursor.execute(query, values)
        except:
            db.rollback()
            return None
        
        cursor.execute("SELECT LAST_INSERT_ID();")
        teamId = cursor.fetchone()[0]
        
        team = cls(name, gameId, teamId)

        if not team.__userJoin(userId, nick, rank, maxRank, "Captain", cursor, db):
            db.rollback()
            return None
        db.commit()
        return team

    @classmethod
    @dbConn()
    def getById(cls, teamId, cursor, db):
        query = "SELECT name, gameId, joinString,teamId FROM teams WHERE teamId=%s"
        cursor.execute(query, (teamId,))
        row = cursor.fetchone()
        if not row:
            return None
        return cls(name=row[0], gameId=row[1], joinString=row[2], teamId=row[3])
    
    @classmethod
    @dbConn()
    def getByName(cls, name, cursor, db):
        query = "SELECT name, gameId, joinString, teamId FROM teams WHERE name=%s"
        cursor.execute(query, (name))
        row = cursor.fetchOneWithNames()
        if not row:
            return None 
        return cls(name=row["name"], gameId=row["gameId"], joinString=row["joinString"], teamId=row["teamId"], dbsync=False)

    @classmethod
    @dbConn()
    def listUsersTeams(self, userId, cursor, db):
        query = 'SELECT `teamId`, `nick`, `role` FROM `registrations` WHERE `userId`=%(userId)s'
        cursor.execute(query, {"userId": userId})
        result = fetchAllWithNames(cursor)
        return result

    @dbConn(autocommit=False, buffered=True)
    def join(self, userId, nick, rank, maxRank, role, cursor, db):
        return self.__userJoin(userId, nick, rank, maxRank, role, cursor, db)
    
    @dbConn(autocommit=True, buffered=False)
    def leave(self, userId, cursor, db):
        query = "DELETE FROM `registrations` WHERE `userId` = %(userId)s AND `teamId` = %(teamId)s LIMIT 1"
        values = {"userId":userId, "teamId":self.teamId}
        cursor.execute(query, values)
        if cursor.rowcount != 1:
            return False
        return True

    def getGame(self):
        return GameModel.getById(self.gameId)
    
    @dbConn()
    def getPlayers(self, cursor, db):
        query = "SELECT `userid`, `nick`, `role`  FROM `registrations` WHERE teamId=%(teamId)s ORDER BY `role` ASC"
        cursor.execute(query, {"teamId": self.teamId})
        result = fetchAllWithNames(cursor)
        return result
    
    @dbConn()
    def generateJoinString(self, cursor, db):
        joinString = genState(200)
        try:
            query = "UPDATE `teams` SET `joinString` = %(joinString)s WHERE `teamId` = %(teamId)s;"
            cursor.execute(query, {"joinString":  joinString, "teamId": self.teamId})
            self.joinString = joinString
            return joinString
        except:
            return None
    
    @dbConn()
    def getUsersRole(self, userId, cursor, db):
        query = 'SELECT role FROM `registrations` WHERE `teamId`=%(teamId)s AND `userId`=%(userId)s'
        cursor.execute(query, {"teamId": self.teamId, "userId": userId})
        result = fetchOneWithNames(cursor)
        if(result):
            return result["role"]
        else:
            return None

    def __userJoin(self, userId, nick, rank, maxRank, role, cursor, db):
        try:
            game = self.getGame()
            query = "INSERT INTO registrations (userId, teamId, nick, role, rank, maxRank) VALUES (%(userId)s, %(teamId)s, %(nick)s, %(role)s, %(rank)s, %(maxRank)s)"
            values = {"userId": userId, "teamId": self.teamId, "nick": nick, "role": role, "rank": rank, "maxRank": maxRank}
            cursor.execute(query, values)
        except IntegrityError:
            return False
        
        query = "SELECT COUNT(*) FROM registrations WHERE teamId=%(teamId)s and role=%(role)s"
        values = {"teamId":self.teamId,"role":role}
        cursor.execute(query, values)
        row = cursor.fetchone()
        if(row[0] > getattr(game, "max"+role+"s")):
            db.rollback()
            return False

        else:
            db.commit()
            return True