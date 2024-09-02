from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn, genState, ObjectDbSync, DatabaseError
from .game import GameModel
from .user import UserModel
from .generatedRole import GeneratedRoleModel
from mysql import connector

class TeamModel(ObjectDbSync):
    tableName = "teams"
    tableId = "teamId"

    def __init__(self, name, gameId, teamId, joinString=None):
        self.name = name
        self.gameId = gameId
        self.teamId = teamId
        self.joinString = joinString
        super().__init__()

    def toDict(self):
        return {
            "teamId": self.teamId,
            "gameId": self.gameId,
            "name": self.name,
            "joinString": self.joinString
        }

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
        try:
            team = cls(name, gameId, cursor.lastrowid)
            defaultGeneratedRoleId = GeneratedRoleModel.getDefaultForGame(gameId)
            team.__userJoin(userId, nick, rank, maxRank, defaultGeneratedRoleId, cursor, db)
        except DatabaseError as e:
            db.rollback()
            raise
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
    def listUsersTeams(self, userId, withJoinstring, cursor, db):
        query = ""
        if withJoinstring:
            query = 'SELECT teamId, nick, generatedRoleId, name, gameId, joinString FROM `teamInfo` WHERE userId=%(userId)s'
        else:
            query = 'SELECT teamId, nick, generatedRoleId, name, gameId FROM `teamInfo` WHERE userId=%(userId)s'

        cursor.execute(query, {"userId": userId})
        result = fetchAllWithNames(cursor)
        return result

    @dbConn(autocommit=True, buffered=True)
    def join(self, userId, nick, rank, maxRank, generatedRoleId, cursor, db):
        return self.__userJoin(userId, nick, rank, maxRank, generatedRoleId, cursor, db)

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
        query = "SELECT `userid`, `nick`, `generatedRoleId`  FROM `registrations` WHERE teamId=%(teamId)s ORDER BY `generatedRoleId` ASC"
        cursor.execute(query, {"teamId": self.teamId})
        fetched = fetchAllWithNames(cursor)
        result = []
        for player in fetched:
            result.append({
                'userid': str(player['userid']),
                'nick': str(player['nick']),
                'generatedRoleId': str(player['generatedRoleId'])
            })
        return result

    @classmethod
    @dbConn()
    def listParticipatingTeams(self, gameId, withDetails, withDiscord, cursor, db):
        game = GameModel.getById(gameId)
        if game is None:
            return None
        else:
            query = ""
            if withDetails is True:
                query += "SELECT teamId, name, userId, nick, generatedRoleId, canPlaySince, rank, maxRank FROM eligibleTeams WHERE gameId = %(gameId)s ORDER BY canPlaySince"
            else:
                query += "SELECT teamId, name, nick, generatedRoleId, canPlaySince FROM eligibleTeams WHERE gameId = %(gameId)s ORDER BY canPlaySince"
            cursor.execute(query, {"gameId": game.gameId})
            result = fetchAllWithNames(cursor)
            if withDetails is True:
                for user in result:
                    user["userId"] =  str(user["userId"])
                    if withDiscord is True:
                        userObject = UserModel.getById(user["userId"])
                        try:
                            user["discordUserObject"] = userObject.getDiscordUserObject()
                        except:
                            user["discordUserObject"] = ""
            for user in result:
                if user["canPlaySince"] is not None:
                    user["canPlaySince"] = user["canPlaySince"].isoformat()
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
        query = 'SELECT generatedRoleId FROM `registrations` WHERE `teamId`=%(teamId)s AND `userId`=%(userId)s'
        cursor.execute(query, {"teamId": self.teamId, "userId": userId})
        result = fetchOneWithNames(cursor)
        if(result):
            return result["generatedRoleId"]
        else:
            return None

    def __userJoin(self, userId, nick, rank, maxRank, generatedRoleId, cursor, db):
        try:
            game = self.getGame()
            query = "INSERT INTO registrations (userId, teamId, nick, generatedRoleId, rank, maxRank) VALUES (%(userId)s, %(teamId)s, %(nick)s, %(generatedRoleId)s, %(rank)s, %(maxRank)s)"
            values = {"userId": userId, "teamId": self.teamId, "nick": nick, "generatedRoleId": generatedRoleId, "rank": rank, "maxRank": maxRank}
            cursor.execute(query, values)
        except connector.DatabaseError as e:
            if e.sqlstate == "45000" and e.msg == 'Already registered for game':
                raise DatabaseError("Already registered for game")
            elif e.sqlstate == "45000" and e.msg == 'Already registered for game':
                raise DatabaseError("No space for this role in this team")
            raise
