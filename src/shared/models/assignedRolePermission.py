from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class AssignedRolePermissionModel(ObjectDbSync):
    tableName = "assignedRolePermissions"
    tableId = "assignedRolePermissionId"

    def __init__(self, assignedRolePermissionId: int, permission: str, assignedRoleId: int, gameId: int):
        self.assignedRolePermissionId = assignedRolePermissionId
        self.permission = permission
        self.assignedRoleId = assignedRoleId
        self.gameId = gameId
        super().__init__()

    def toDict(self):
        return {
            "assignedRolePermissionId": self.assignedRolePermissionId,
            "permission": self.permission,
            "assignedRoleId": self.assignedRoleId,
            "gameId": self.gameId
        }

    @classmethod
    @dbConn()
    def create(cls, permission, assignedRoleId, gameId, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`permission`, `assignedRoleId`, `gameId`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (permission, assignedRoleId, gameId))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(assignedRolePermissionId=cursor.lastrowid, permission=permission, assignedRoleId=assignedRoleId, gameId=gameId)
