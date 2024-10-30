from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import datetime
from ..utils import ObjectDbSync

class GameModel(ObjectDbSync):
    """Representation of game

    Attributes:
            gameId (int): id of game
            name (str): name of game
            registrationStart (datetime): date of start of registration for this game
            registrationEnd (datetime): date of end of registration for this game
            gamePage (str): page for this game
            maxTeams (int): maximum teams for this game
            backdrop (str|None): backdrop url for this game
            icon (str|None): icon url for this game
    """
    tableName = "games"
    tableId = "gameId"

    def __init__(self, name=None, registrationStart=datetime.now(), registrationEnd=datetime.now(), gameId=None, gamePage=None, maxTeams=None, backdrop=None, icon=None):
        """Initializes representation of game

        Args:
            gameId (int): id of game
            name (str): name of game
            registrationStart (date): date of start of registration for this game
            registrationEnd (date): date of end of registration for this game
            gamePage (str): page for this game
            maxTeams (int): maximum teams for this game
            backdrop (str|None): backdrop url for this game
            icon (str|None): icon url for this game
        """
        self.gameId = gameId
        self.name = name
        self.registrationStart = registrationStart
        self.registrationEnd = registrationEnd
        self.gamePage = gamePage
        self.maxTeams = maxTeams
        self.backdrop = backdrop
        self.icon = icon
        super().__init__()

    def canBeRegistered(self):
        """Returns if game can be registered
            <registrationStart, registrationEnd)
        Returns:
            bool: can be registered
        """
        return (datetime.now() >= self.registrationStart) & (datetime.now() <= self.registrationEnd)

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
            "maxTeams": self.maxTeams,
            "backdrop": self.backdrop,
            "icon": self.icon
        }

    def __str__(self):
        return dumps(self.toDict())

    @classmethod
    @dbConn()
    def create(cls, name: str, registrationStart: datetime, registrationEnd: datetime, maxTeams: int, backdrop: str, icon: str, cursor, db):
        """Initializes representation of game

        Args:
            gameId (int): id of game
            name (str): name of game
            registrationStart (datetime): date of start of registration for this game
            registrationEnd (datetime): date of end of registration for this game
            maxTeams (int): maximum teams for this game
        Returns:
            GameModel: representation of game
        """
        query = "INSERT INTO games (name, registrationStart, registrationEnd, maxTeams, backdrop, icon) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, registrationStart, registrationEnd, maxTeams, backdrop, icon))
        return cls(gameId=cursor.lastrowid, name=name, registrationStart=registrationStart, registrationEnd=registrationEnd, maxTeams=maxTeams, backdrop=backdrop, icon=icon)

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
