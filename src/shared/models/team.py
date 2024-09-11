from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn, genState, ObjectDbSync, DatabaseError
from .game import GameModel
from .user import UserModel
from .generatedRole import GeneratedRoleModel
from mysql import connector
from typing import Union

class TeamModel(ObjectDbSync):
    """Representation of Team

    Attributes:
            teamId (int): id of team
            name (str): name team
            gameId (int): id of game team is participating in
            joinString (Union[str, None]): secret string that users use to join team
    """
    tableName = "teams"
    tableId = "teamId"

    def __init__(self, name: str, gameId: int, teamId: int, joinString: Union[str, None]=None):
        """Initializes representation of Team

        Args:
            teamId (int): id of team
            name (str): team name
            gameId (int): id of game team is participating in
            joinString (Union[str, None]): secret string that users use to join team
        """
        self.name = name
        self.gameId = gameId
        self.teamId = teamId
        self.joinString = joinString
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "teamId": self.teamId,
            "gameId": self.gameId,
            "name": self.name,
            "joinString": self.joinString
        }

    @classmethod
    @dbConn(autocommit=False, buffered=True)
    def create(cls, name: str, gameId: int, userId: int, nick: str, rank: int, maxRank: int, cursor, db):
        """Creates new team

        Args:
            name (str): team name
            gameId (int): id of game team is participating in
            userId (int): id of user who wants to create this team
            nick (str): nick of user who wants to create this team
            rank (int): rank of user who wants to create this team
            maxRank (int): maximal rank of user who wants to create this team

        Raises:
            DatabaseError: Already registered for game.
            DatabaseError: No space for this role in this team.

        Returns:
            Union[TeamModel, None]: new team
        """
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
    def getById(cls, teamId: int, cursor, db):
        """Gets team by id

        Args:
            teamId (int): teamId

        Returns:
            [TeamModel, None]: team
        """
        query = "SELECT name, gameId, joinString,teamId FROM teams WHERE teamId=%s"
        cursor.execute(query, (teamId,))
        row = cursor.fetchone()
        if not row:
            return None
        return cls(name=row[0], gameId=row[1], joinString=row[2], teamId=row[3])

    @classmethod
    @dbConn()
    def getByName(cls, name, cursor, db):
        """Gets team by name

        Args:
            name (str): name of the team
        Returns:
            Union[TeamModel, None]: team
        """
        query = "SELECT name, gameId, joinString, teamId FROM teams WHERE name=%s"
        cursor.execute(query, (name))
        row = cursor.fetchOneWithNames()
        if not row:
            return None
        return cls(name=row["name"], gameId=row["gameId"], joinString=row["joinString"], teamId=row["teamId"], dbsync=False)

    @classmethod
    @dbConn()
    def listUsersTeams(self, userId, withJoinstring, cursor, db):
        """List teams user is part of

        Args:
            userId (int): id of user
            withJoinstring (bool): should JoinString be included

        Returns:
            list[dict]: list of dict of teams (key = column name)
        """
        query = ""
        if withJoinstring:
            query = 'SELECT teamId, nick, generatedRoleId, name, gameId, joinString FROM `teamInfo` WHERE userId=%(userId)s'
        else:
            query = 'SELECT teamId, nick, generatedRoleId, name, gameId FROM `teamInfo` WHERE userId=%(userId)s'

        cursor.execute(query, {"userId": userId})
        result = fetchAllWithNames(cursor)
        return result

    @dbConn(autocommit=True, buffered=True)
    def join(self, userId: int, nick: str, rank: int, maxRank: int, generatedRoleId: int, cursor, db):
        """Add user to this team

        Args:
            userId (int): id of user who wants to join this team
            nick (str): mick of user who wants to join this team
            rank (int): rank of user who wants to join this team
            maxRank (int): maximal rank of user who wants to join this team
            generatedRoleId (int): role that use wants to play in team

        Raises:
            DatabaseError: Already registered for game.
            DatabaseError: No space for this role in this team.

        Returns:
            None: nothing
        """
        return self.__userJoin(userId, nick, rank, maxRank, generatedRoleId, cursor, db)

    @dbConn(autocommit=True, buffered=False)
    def leave(self, userId, cursor, db):
        """Removes user from this team

        Args:
            userId (int): id of user to remove

        Returns:
            bool: was removed
        """
        query = "DELETE FROM `registrations` WHERE `userId` = %(userId)s AND `teamId` = %(teamId)s LIMIT 1"
        values = {"userId":userId, "teamId":self.teamId}
        cursor.execute(query, values)
        if cursor.rowcount != 1:
            return False
        return True

    def getGame(self):
        """Returns game of this team

        Returns:
            GameModel: game of this team
        """
        return GameModel.getById(self.gameId)

    @dbConn()
    def getPlayers(self, cursor, db):
        """Gets list of players of this team

        Returns:
            list[dict]: list of dicts of players (key = column name)
        """
        query = "SELECT `userId`, `nick`, `generatedRoleId`  FROM `registrations` WHERE teamId=%(teamId)s ORDER BY `generatedRoleId` ASC"
        cursor.execute(query, {"teamId": self.teamId})
        fetched = fetchAllWithNames(cursor)
        result = []
        for player in fetched:
            result.append({
                'userId': str(player['userId']),
                'nick': str(player['nick']),
                'generatedRoleId': player['generatedRoleId']
            })
        return result

    @classmethod
    @dbConn()
    def listParticipatingTeams(self, gameId: int, withDetails: bool, withDiscord: bool, cursor, db):
        """List teams that are able to participate in tournament in order of completion of requirements

        Args:
            gameId (int): _description_
            withDetails (bool): list additional sensitive details
            withDiscord (bool): get discord user info (slow because has to be fetched from discord api)

        Returns:
            list[dict]: list of dicts of teams (key = column name)
        """
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
        """Generate joinString

        Returns:
            Union[str, None]: new joinString
        """
        joinString = genState(200)
        try:
            query = "UPDATE `teams` SET `joinString` = %(joinString)s WHERE `teamId` = %(teamId)s;"
            cursor.execute(query, {"joinString":  joinString, "teamId": self.teamId})
            self.joinString = joinString
            return joinString
        except:
            return None

    @dbConn()
    def getUsersRole(self, userId: int, cursor, db):
        """Gets role of user in this team

        Args:
            userId (int): _description_

        Returns:
            Union[none, int]: role of user in this team
        """
        query = 'SELECT generatedRoleId FROM `registrations` WHERE `teamId`=%(teamId)s AND `userId`=%(userId)s'
        cursor.execute(query, {"teamId": self.teamId, "userId": userId})
        result = fetchOneWithNames(cursor)
        if(result):
            return result["generatedRoleId"]
        else:
            return None

    def __userJoin(self, userId: int, nick: str, rank: int, maxRank: int, generatedRoleId: int, cursor, db):
        """Tries to join user to team

        Args:
            userId (int): id of user who wants to join this team
            nick (str): mick of user who wants to join this team
            rank (int): rank of user who wants to join this team
            maxRank (int): maximal rank of user who wants to join this team
            generatedRoleId (int): role that use wants to play in team

        Raises:
            DatabaseError: Already registered for game.
            DatabaseError: No space for this role in this team.
        """
        try:
            game = self.getGame()
            query = "INSERT INTO registrations (userId, teamId, nick, generatedRoleId, rank, maxRank) VALUES (%(userId)s, %(teamId)s, %(nick)s, %(generatedRoleId)s, %(rank)s, %(maxRank)s)"
            values = {"userId": userId, "teamId": self.teamId, "nick": nick, "generatedRoleId": generatedRoleId, "rank": rank, "maxRank": maxRank}
            cursor.execute(query, values)
        except connector.DatabaseError as e:
            if e.sqlstate == "45000" and e.msg == 'Already registered for game':
                raise DatabaseError("Already registered for game.")
            elif e.sqlstate == "45000" and e.msg == 'No space for this role in this team':
                raise DatabaseError("No space for this role in this team.")
            raise
