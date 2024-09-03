from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class AssignedRoleModel(ObjectDbSync):
    tableName = "assignedRoles"
    tableId = "assignedRoleId"

    def __init__(self, assignedRoleId: int, roleName: str, discordRoleId: int):
        self.assignedRoleId = assignedRoleId
        self.roleName = roleName
        self.discordRoleId = discordRoleId
        super().__init__()

    def toDict(self):
        return {
            "assignedRoleId": self.assignedRoleId,
            "roleName": self.roleName,
            "discordRoleId": self.discordRoleId
        }

    @classmethod
    @dbConn()
    def create(cls, roleName, discordRoleId, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`roleName`, `discordRoleId`) VALUES (%s, %s)"
        try:
            cursor.execute(query, (roleName, discordRoleId))
        except IntegrityError as e:
            raise ValueError("Role with this name already exists")
        return cls(assignedRoleId=cursor.lastrowid, roleName=roleName, discordRoleId=discordRoleId)
