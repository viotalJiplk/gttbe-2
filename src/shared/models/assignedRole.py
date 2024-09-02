from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class AssignedRoleModel(ObjectDbSync):
    tableName = "rolePermissions"
    tableId = "assignedRoleId"

    def __init__(self, assignedRoleId, permission, roleId):
        self.assignedRoleId = assignedRoleId
        self.permission = permission
        self.discordRoleId = discordRoleId

    def toDict(self):
        return {
            "assignedRoleId": self.assignedRoleId,
            "permission": self.permission,
            "discordRoleId": self.discordRoleId
        }

    @classmethod
    @dbConn()
    def create(cls, permission, discordRoleId, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`permission`, `discordRoleId`) VALUES (%s, %s)"
        try:
            cursor.execute(query, (permission, discordRoleId))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(assignedRoleId=cursor.lastrowid, permission=permission, discordRoleId=discordRoleId)
