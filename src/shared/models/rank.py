from ..utils import fetchAllWithNames, dbConn
from json import dumps
from ..utils import ObjectDbSync

class RankModel(ObjectDbSync):
    """Representation of rank

    Attributes:
            rankId (int): id of rank
            rankName (str): name of rank
            gameId (int): gameId of game this rank belongs to
    """
    tableName = "ranks"
    tableId = "rankId"

    def __init__(self, rankId: int, rankName: str, gameId: int):
        """Initializes representation of game

        Args:
            rankId (int): id of rank
            rankName (str): name of rank
            gameId (int): gameId of game this rank belongs to
        """
        self.rankId = rankId
        self.rankName = rankName
        self.gameId = gameId
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "rankId": self.rankId,
            "rankName": self.rankName,
            "gameId": self.gameId,
        }

    def __str__(self):
        return dumps(self.toDict())

    @classmethod
    @dbConn()
    def create(cls, rankName: str, gameId: int, cursor, db):
        """Initializes representation of game

        Args:
            rankName (str): name of rank
            gameId (int): gameId of game this rank belongs to
        Returns:
            RankModel: representation of rank
        """
        query = f"INSERT INTO `{cls.tableName}` (rankName, gameId) VALUES (%s, %s)"
        cursor.execute(query, (rankName, gameId))
        return cls(rankId=cursor.lastrowid, rankName=rankName,gameId=gameId)

    @classmethod
    @dbConn()
    def getDictByGame(cls, gameId: int, cursor, db):
        """
            Returns list of dict of all games in db

            Returns:
                list[dict]: list dict of all games (key = colum name)
        """
        query = f"SELECT * FROM `{cls.tableName}` WHERE gameId=%s;"
        cursor.execute(query, (gameId, ))
        return fetchAllWithNames(cursor)
