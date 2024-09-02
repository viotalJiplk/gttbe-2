from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class GeneratedRolePermissionModel(ObjectDbSync):
    tableName = "generatedRolePermissionsId"
    tableId = "generatedRolePermissions"

    def __init__(self, generatedRolePermissionsId, permission, generatedRoleId, gameId, eligible):
        self.generatedRolePermissionsId = generatedRolePermissionsId
        self.permission = permission
        self.generatedRoleId = generatedRoleId
        self.gameId = gameId
        self.eligible = eligible

    def toDict(self):
        return {
            "generatedRolePermissionsId": self.generatedRolePermissionsId,
            "permission": self.permission,
            "generatedRoleId": self.generatedRoleId,
            "gameId": self.gameId,
            "eligible": self.eligible
        }

    @classmethod
    @dbConn()
    def create(cls, permission, generatedRoleId, gameId, eligible, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`permission`, `generatedRoleId`, `gameId`, `eligible`) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (permission, generatedRoleId, gameId, eligible))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(generatedRolePermissionsId=cursor.lastrowid, permission=permission, generatedRoleId=generatedRoleId, gameId=gameId, eligible=eligible)
