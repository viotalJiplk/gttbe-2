from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class UserRoleModel(ObjectDbSync):
    tableName = "userRoles"
    tableId = "userRoleId"

    def __init__(self, userRoleId, roleId, userId, gameId):
        self.userRoleId = userRoleId
        self.roleId = roleId
        self.userId = userId
        super().__init__()

    def toDict(self):
        return {
            "userRoleId": self.userRoleId,
            "roleId": self.roleId,
            "userId": self.userId
        }

    @classmethod
    @dbConn()
    def create(cls, roleId, userId, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`roleId`, `userId`) VALUES (%s, %s)"
        try:
            cursor.execute(query, (roleId, userId))
        except IntegrityError as e:
            raise ValueError("This userRole already exists.")
        return cls(userRoleId=cursor.lastrowid, roleId=roleId, userId=userId, gameId=gameId)
