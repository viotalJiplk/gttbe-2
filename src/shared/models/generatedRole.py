from ..utils import ObjectDbSync, dbConn, fetchOneWithNames, fetchAllWithNames
from typing import Union

class GeneratedRoleModel(ObjectDbSync):
    """Representation of generatedRole

    Attributes:
            generatedRoleId (int): id of generatedRole
            roleName (str): name of generatedRole
            discordRoleId (Union[int, None]): id of role on discord when team is not eligible to be in tournament
            discordRoleIdEligible (Union[int, None]): id of role on discord when team is eligible to be in tournament
            gameId (int): id of game which this role belongs to
            default (bool): is this the default (role that the creator of team gets) role for this game
            minimal (int): minimal number of players with this role in team for team to be eligible to be part of tournament
            maximal (int): maximal number of players with this role in team
    """
    tableName = "generatedRoles"
    tableId = "generatedRoleId"

    def __init__(self, generatedRoleId: int, roleName: str, discordRoleId: Union[int, None], discordRoleIdEligible: Union[int, None], gameId: int, default: bool, minimal: int, maximal: int):
        """Initializes representation of generatedRole

        Args:
            generatedRoleId (int): id of generatedRole
            roleName (str): name of generatedRole
            discordRoleId (Union[int, None]): id of role on discord when team is not eligible to be in tournament
            discordRoleIdEligible (Union[int, None]): id of role on discord when team is eligible to be in tournament
            gameId (int): id of game which this role belongs to
            default (bool): is this the default (role that the creator of team gets) role for this game
            minimal (int): minimal number of players with this role in team for team to be eligible to be part of tournament
            maximal (int): maximal number of players with this role in team
        """
        self.generatedRoleId = generatedRoleId
        self.roleName = roleName
        self.discordRoleId = discordRoleId
        self.discordRoleIdEligible = discordRoleIdEligible
        self.gameId = gameId
        self.default = default
        self.minimal = minimal
        self.maximal = maximal
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        discordRoleId = None
        if self.discordRoleId is not None:
            discordRoleId = str(self.discordRoleId)
        discordRoleIdEligible = None
        if self.discordRoleIdEligible is not None:
            discordRoleIdEligible = str(self.discordRoleIdEligible)
        return {
            "generatedRoleId": self.generatedRoleId,
            "roleName": self.roleName,
            "discordRoleId": discordRoleId,
            "discordRoleIdEligible": discordRoleIdEligible,
            "gameId": self.gameId,
            "default": self.default,
            "minimal": self.minimal,
            "maximal": self.maximal
        }

    @classmethod
    @dbConn()
    def create(cls, roleName: str, discordRoleId: Union[int, None], discordRoleIdEligible: Union[int, None], gameId: int, default: bool, minimal: int, maximal: int, cursor, db):
        """Creates new generatedRole

        Args:
            roleName (str): name of generatedRole
            discordRoleId (Union[int, None]): id of role on discord when team is not eligible to be in tournament
            discordRoleIdEligible (Union[int, None]): id of role on discord when team is eligible to be in tournament
            gameId (int): id of game which this role belongs to
            default (bool): is this the default (role that the creator of team gets) role for this game
            minimal (int): minimal number of players with this role in team for team to be eligible to be part of tournament
            maximal (int): maximal number of players with this role in team

        Raises:
            ValueError: Role with this name already exists

        Returns:
            GeneratedRoleModel: _description_
        """
        query = f"INSERT INTO `{cls.tableName}` (`roleName`, `discordRoleId`, `discordRoleIdEligible`, `gameId`, `default`, `minimal`, `maximal`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (roleName, discordRoleId, discordRoleIdEligible, gameId, default, minimal, maximal))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(generatedRoleId=cursor.lastrowid, roleName=roleName, discordRoleId=discordRoleId, discordRoleIdEligible=discordRoleIdEligible, gameId=gameId, default=default, minimal=minimal, maximal=maximal)

    @classmethod
    @dbConn()
    def getDefaultForGame(cls, gameId: int, cursor, db):
        """Returns default generated role for the game

        Args:
            gameId (int): id of game

        Returns:
            Union[int, None]: generatedRoleId
        """
        query = f"SELECT `generatedRoleId` FROM `{cls.tableName}` WHERE `gameId` = %s AND `default` = CONV('1', 2, 10) + 0"
        cursor.execute(query, (gameId,))
        row = fetchOneWithNames(cursor)
        if row is None:
            return None
        else:
            return row["generatedRoleId"]

    @classmethod
    @dbConn()
    def getAllDict(self, gameId, cursor, db):
        """Returns list of dict of all generatedRoles in db

            Returns:
                list[dict]: list dict of all generatedRoles (key = colum name)
        """

        if gameId is None:
            query ="""SELECT * FROM generatedRoles AS gr"""
            cursor.execute(query)
        else:
            query ="""SELECT * FROM generatedRoles AS gr WHERE gr.gameId =%(gameId)s"""
            cursor.execute(query,  {'gameId': gameId})
        return fetchAllWithNames(cursor)

    @dbConn()
    def listPermissions(self, cursor, db):
        """List all permissions that belongs to this role

        Returns:
            list[dict]: list of permissions
        """
        query ="""SELECT grp.* FROM generatedRoles AS gr
                    INNER JOIN generatedRolePermissions AS grp ON gr.generatedRoleId = grp.generatedRoleId
                    INNER JOIN permissions AS p ON p.permission = grp.permission WHERE gr.generatedRoleId = %(generatedRoleId)s"""
        cursor.execute(query,  {'generatedRoleId': self.generatedRoleId})
        return fetchAllWithNames(cursor)
