from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class GeneratedRolePermissionModel(ObjectDbSync):
    tableName = "generatedRolePermissions"
    tableId = "generatedRolePermissionId"

    def __init__(self, generatedRolePermissionId: int, permission: str, generatedRoleId: int, gameId: int, eligible: bool):
        self.generatedRolePermissionId = generatedRolePermissionId
        self.permission = permission
        self.generatedRoleId = generatedRoleId
        self.gameId = gameId
        self.eligible = eligible
        super().__init__()

    def toDict(self):
        return {
            "generatedRolePermissionId": self.generatedRolePermissionId,
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
        return cls(generatedRolePermissionId=cursor.lastrowid, permission=permission, generatedRoleId=generatedRoleId, gameId=gameId, eligible=eligible)
