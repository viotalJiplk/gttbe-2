from ..utils import dbConn
from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync, fetchAllWithNames
from typing import Union

class AssignedRoleModel(ObjectDbSync):
    """Representation of assignedRole

    Attributes:
            assignedRoleId (int): id of assignedRole
            roleName (str): name of assignedRole
            discordRoleId (Union[int, None]): id of role on discord
    """
    tableName = "assignedRoles"
    tableId = "assignedRoleId"

    def __init__(self, assignedRoleId: int, roleName: str, discordRoleId: Union[int, None]):
        """ Initializes representation of assignedRole

        Args:
            assignedRoleId (int): id of assignedRole
            roleName (str): name of assignedRole
            discordRoleId (Union[int, None]): id of role on discord
        """
        self.assignedRoleId = assignedRoleId
        self.roleName = roleName
        self.discordRoleId = discordRoleId
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "assignedRoleId": self.assignedRoleId,
            "roleName": self.roleName,
            "discordRoleId": self.discordRoleId
        }

    @classmethod
    @dbConn()
    def create(cls, roleName, discordRoleId, cursor, db):
        """Creates new assignedRole

        Args:
            roleName (str): name of assignedRole
            discordRoleId (Union[int, None]): id of role on discord

        Raises:
            ValueError: AssignedRole with this name already exists.

        Returns:
            AssignedRoleModel: Representation of new assignedRole.
        """
        query = f"INSERT INTO `{cls.tableName}` (`roleName`, `discordRoleId`) VALUES (%s, %s)"
        try:
            cursor.execute(query, (roleName, discordRoleId))
        except IntegrityError as e:
            raise ValueError("AssignedRole with this name already exists.")
        return cls(assignedRoleId=cursor.lastrowid, roleName=roleName, discordRoleId=discordRoleId)

    @dbConn()
    def listPermissions(self, cursor, db):
        """List all permissions that belongs to this role

        Returns:
            list[dict]: list of permissions
        """
        query ="""SELECT arp.* FROM assignedRoles AS ar
                    INNER JOIN assignedRolePermissions AS arp ON ar.assignedRoleId = arp.assignedRoleId
                    INNER JOIN permissions AS p ON p.permission = arp.permission WHERE ar.assignedRoleId = %(assignedRoleId)s"""
        cursor.execute(query,  {'assignedRoleId': self.assignedRoleId})
        return fetchAllWithNames(cursor)
