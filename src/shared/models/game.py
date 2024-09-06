from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date
from ..utils import ObjectDbSync

class GameModel(ObjectDbSync):
    """Representation of game

    Attributes:
            gameId (int): id of game
            name (str): name of game
            registrationStart (date): date of start of registration for this game
            registrationEnd (date): date of end of registration for this game
            gamePage (str): page for this game
            maxTeams (int): maximum teams for this game
    """
    tableName = "games"
    tableId = "gameId"

    def __init__(self, name=None, registrationStart=date.fromisocalendar(1,1,1), registrationEnd=date.fromisocalendar(9999,1,1), gameId=None, gamePage=None, maxTeams=None):
        """Initializes representation of game

        Args:
            gameId (int): id of game
            name (str): name of game
            registrationStart (date): date of start of registration for this game
            registrationEnd (date): date of end of registration for this game
            gamePage (str): page for this game
            maxTeams (int): maximum teams for this game
        """
        self.gameId = gameId
        self.name = name
        self.registrationStart = registrationStart
        self.registrationEnd = registrationEnd
        self.gamePage = gamePage
        self.maxTeams = maxTeams
        super().__init__()

    def canBeRegistered(self):
        """Returns if game can be registered
            <registrationStart, registrationEnd)
        Returns:
            bool: can be registered
        """
        return (date.today() >= self.registrationStart) & (date.today() < self.registrationEnd)

    def getGamePage(self):
        """Returns page for the game

        Returns:
            str: page for the game
        """
        return self.gamePage

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
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
    def create(cls, name: str, registrationStart: date, registrationEnd: date, maxTeams: int, cursor, db):
        """Initializes representation of game

        Args:
            gameId (int): id of game
            name (str): name of game
            registrationStart (date): date of start of registration for this game
            registrationEnd (date): date of end of registration for this game
            maxTeams (int): maximum teams for this game
        Returns:
            GameModel: representation of game
        """
        query = "INSERT INTO games (name, registrationStart, registrationEnd, maxTeams) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, registrationStart, registrationEnd, maxTeams))
        return cls(gameId=cursor.lastrowid, name=name, registrationStart=registrationStart, registrationEnd=registrationEnd, maxTeams=maxTeams)

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        """
            Returns list of dict of all games in db

            Returns:
                list[dict]: list dict of all games (key = colum name)
        """
        rows = super().getAllDict()
        for index in range(0, len(rows)):
            rows[index]["registrationStart"] = rows[index]["registrationStart"].isoformat()
            rows[index]["registrationEnd"] = rows[index]["registrationEnd"].isoformat()
        return rows
