from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync
from typing import Union

class GeneratedRolePermissionModel(ObjectDbSync):
    """Representation of generatedRolePermission

    Attributes:
            generatedRolePermissionId (int): id of generatedRolePermission
            permission (str): permission
            assignedRoleId (int): id of assignedRole this permission belongs to
            gameId (Union[int, None]): id of game for this permission (None = all)
            eligible (bool): does this apply to members of teams witch are eligible to enter tournament or those who are not
    """
    tableName = "generatedRolePermissions"
    tableId = "generatedRolePermissionId"

    def __init__(self, generatedRolePermissionId: int, permission: str, generatedRoleId: int, gameId: Union[int, None], eligible: bool):
        """Initializes representation of generatedRolePermission

        Args:
            generatedRolePermissionId (int): id of generatedRolePermission
            permission (str): permission
            assignedRoleId (int): id of assignedRole this permission belongs to
            gameId (Union[int, None]): id of game for this permission (None = all)
            eligible (bool): does this apply to members of teams witch are eligible to enter tournament or those who are not
        """
        self.generatedRolePermissionId = generatedRolePermissionId
        self.permission = permission
        self.generatedRoleId = generatedRoleId
        self.gameId = gameId
        self.eligible = eligible
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "generatedRolePermissionId": self.generatedRolePermissionId,
            "permission": self.permission,
            "generatedRoleId": self.generatedRoleId,
            "gameId": self.gameId,
            "eligible": self.eligible
        }

    @classmethod
    @dbConn()
    def create(cls, permission: str, generatedRoleId: int, gameId: Union[int, None], eligible: bool, cursor, db):
        """Creates new generatedRolePermission

        Args:
            generatedRolePermissionId (int): id of generatedRolePermission
            permission (str): permission
            assignedRoleId (int): id of assignedRole this permission belongs to
            gameId (Union[int, None]): id of game for this permission (None = all)
            eligible (bool): does this apply to members of teams witch are eligible to enter tournament or those who are not

        Raises:
            ValueError: generatedRole already has this permission

        Returns:
            GeneratedRolePermissionModel: AssignedRolePermissionModel: Representation of new generatedRolePermission.
        """
        query = f"INSERT INTO `{cls.tableName}` (`permission`, `generatedRoleId`, `gameId`, `eligible`) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (permission, generatedRoleId, gameId, eligible))
        except IntegrityError as e:
            raise ValueError("GeneratedRole already has this permission.")
        return cls(generatedRolePermissionId=cursor.lastrowid, permission=permission, generatedRoleId=generatedRoleId, gameId=gameId, eligible=eligible)
