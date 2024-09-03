from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class UserRoleModel(ObjectDbSync):
    tableName = "userRoles"
    tableId = "userRoleId"

    def __init__(self, userRoleId: int, assignedRoleId: int, userId: str):
        self.userRoleId = userRoleId
        self.assignedRoleId = assignedRoleId
        self.userId = userId
        super().__init__()

    def toDict(self):
        return {
            "userRoleId": self.userRoleId,
            "assignedRoleId": self.assignedRoleId,
            "userId": str(self.userId)
        }

    @classmethod
    @dbConn()
    def create(cls, assignedRoleId, userId, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (`assignedRoleId`, `userId`) VALUES (%s, %s)"
        try:
            cursor.execute(query, (assignedRoleId, userId))
        except IntegrityError as e:
            raise ValueError("This userRole already exists.")
        return cls(userRoleId=cursor.lastrowid, assignedRoleId=assignedRoleId, userId=userId)
