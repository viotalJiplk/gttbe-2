from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class AssignedRolePermissionModel(ObjectDbSync):
    tableName = "assignedRolePermissions"
    tableId = "rolePermissionId"

    def __init__(self, rolePermissionId, permission, assignedRoleId, gameId):
        self.rolePermissionId = rolePermissionId
        self.permission = permission
        self.assignedRoleId = assignedRoleId
        self.gameId = gameId

    def toDict(self):
        return {
            "rolePermissionId": self.rolePermissionId,
            "permission": self.permission,
            "assignedRoleId": self.assignedRoleId,
            "gameId": self.gameId
        }

    @classmethod
    @dbConn()
    def create(cls, permission, assignedRoleId, gameId, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`permission`, `assignedRoleId`, `gameId`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (permission, discordRoleId))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(rolePermissionId=cursor.lastrowid, permission=permission, assignedRoleId=assignedRoleId, gameId=gameId)
