from ..utils import ObjectDbSync, dbConn, fetchOneWithNames, fetchAllWithNames

class GeneratedRoleModel(ObjectDbSync):
    tableName = "generatedRoles"
    tableId = "generatedRoleId"

    def __init__(self, generatedRoleId: int, roleName: str, discordRoleId: int, discordRoleIdEligible: int, gameId: int, default: bool, minimal: int, maximal: int):
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
    def create(cls, roleName: str, discordRoleId: int, discordRoleIdEligible: int, gameId: int, default: bool, minimal: int, maximal: int, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`roleName`, `discordRoleId`, `discordRoleIdEligible`, `gameId`, `default`, `minimal`, `maximal`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (roleName, discordRoleId, discordRoleIdEligible, gameId, default, minimal, maximal))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(generatedRoleId=cursor.lastrowid, roleName=roleName, discordRoleId=discordRoleId, discordRoleIdEligible=discordRoleIdEligible, gameId=gameId, default=default, minimal=minimal, maximal=maximal)

    @classmethod
    @dbConn()
    def getDefaultForGame(cls, gameId: int, cursor, db):
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
        if gameId is None:
            query ="""SELECT * FROM generatedRoles AS gr"""
            cursor.execute(query)
        else:
            query ="""SELECT * FROM generatedRoles AS gr WHERE gr.gameId =%(gameId)s"""
            cursor.execute(query,  {'gameId': gameId})
        return fetchAllWithNames(cursor)

    @dbConn()
    def listPermissions(self, cursor, db):
        query ="""SELECT grp.* FROM generatedRoles AS gr
                    INNER JOIN generatedRolePermissions AS grp ON gr.generatedRoleId = grp.generatedRoleId
                    INNER JOIN permissions AS p ON p.permission = grp.permission WHERE gr.generatedRoleId = %(generatedRoleId)s"""
        cursor.execute(query,  {'generatedRoleId': self.generatedRoleId})
        return fetchAllWithNames(cursor)
