from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync
from typing import Union

class AssignedRolePermissionModel(ObjectDbSync):
    """Representation of assignedRolePermission

    Attributes:
            assignedRolePermissionId (int): id of assignedRolePermission
            permission (str): permission
            assignedRoleId (int): id of assignedRole this permission belongs to
            gameId (Union[int, None]): id of game for this permission (None = all)
    """
    tableName = "assignedRolePermissions"
    tableId = "assignedRolePermissionId"

    def __init__(self, assignedRolePermissionId: int, permission: str, assignedRoleId: int, gameId: Union[int, None]):
        """ Initializes representation of assignedRolePermission

        Args:
            assignedRolePermissionId (int): id of assignedRolePermission
            permission (str): permission
            assignedRoleId (int): id of assignedRole this permission belongs to
            gameId (Union[int, None]): id of game for this permission (None = all)
        """
        self.assignedRolePermissionId = assignedRolePermissionId
        self.permission = permission
        self.assignedRoleId = assignedRoleId
        self.gameId = gameId
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "assignedRolePermissionId": self.assignedRolePermissionId,
            "permission": self.permission,
            "assignedRoleId": self.assignedRoleId,
            "gameId": self.gameId
        }

    @classmethod
    @dbConn()
    def create(cls, permission: str, assignedRoleId: int, gameId: Union[int, None], cursor, db):
        """Creates new assignedRolePermission

        Args:
            permission (str): permission
            assignedRoleId (int): id of assignedRole this permission belongs to
            gameId (Union[int, None]): id of game for this permission (None = all)

        Raises:
            ValueError: assignedRole already has this permission

        Returns:
            AssignedRolePermissionModel: Representation of new assignedRolePermission.
        """
        query = f"INSERT INTO `{cls.tableName}` (`permission`, `assignedRoleId`, `gameId`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (permission, assignedRoleId, gameId))
        except IntegrityError as e:
            raise ValueError("AssignedRole already has this permission.")
        return cls(assignedRolePermissionId=cursor.lastrowid, permission=permission, assignedRoleId=assignedRoleId, gameId=gameId)
