from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync

class UserRoleModel(ObjectDbSync):
    """Represents users assignedRole

    Attributes:

    """
    tableName = "userRoles"
    tableId = "userRoleId"

    def __init__(self, userRoleId: int, assignedRoleId: int, userId: str):
        """Initialize representation of users assignedRole

        Args:
            userRoleId (int): id of userRole
            assignedRoleId (int): id of assignedRole
            userId (str): id of user
        """
        self.userRoleId = userRoleId
        self.assignedRoleId = assignedRoleId
        self.userId = userId
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "userRoleId": self.userRoleId,
            "assignedRoleId": self.assignedRoleId,
            "userId": str(self.userId)
        }

    @classmethod
    @dbConn()
    def create(cls, assignedRoleId: int, userId: int, cursor, db):
        """Creates new users assignedRole

        Args:
            assignedRoleId (int): id of assignedRole
            userId (int): id of user

        Raises:
            ValueError: This userRole already exists.

        Returns:
            UserRoleModel: new users assignedRole
        """
        query = f"INSERT INTO `{cls.tableName}` (`assignedRoleId`, `userId`) VALUES (%s, %s)"
        try:
            cursor.execute(query, (assignedRoleId, userId))
        except IntegrityError as e:
            raise ValueError("This userRole already exists.")
        return cls(userRoleId=cursor.lastrowid, assignedRoleId=assignedRoleId, userId=userId)
