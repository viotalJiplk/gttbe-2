from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync
from ..utils import dbConn, fetchAllWithNames
from typing import Union, List
from ..models.user import UserModel

class PermissionModel(ObjectDbSync):
    """Representation of permission

    Attributes:
            permission (str): name of permission
    """
    tableName = "permissions"
    tableId = "permission"

    def __init__(self, permission: str):
        """_Initializes representation of permission

        Args:
            permission (str): name of permission
        """
        self.permission = permission
        super().__init__()


    @classmethod
    @dbConn()
    def create(cls, permission: str, cursor, db):
        """Creates new permission

        Args:
            permission (str): name of permission

        Raises:
            ValueError: This permission already exists.

        Returns:
            PermissionModel: new permission
        """
        query = f"INSERT INTO `{cls.tableName}` (permission) VALUES (%s)"
        try:
            cursor.execute(query, (permission,))
        except IntegrityError as e:
            raise ValueError("This permission already exists.")
        return cls(permission)

    @classmethod
    @dbConn()
    def listPublic(cls, gameId: Union[str, None], cursor, db):
        """Lists all public permission

        Args:
            gameId (Union[str, None]): id of game for which you want permissions (None = only for all games)
        Returns:
            list[dict]: list of dict of permissions
        """
        if(gameId is None):
            query = """SELECT p.permission, arp.gameId FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public')
) AND gameId IS NULL;"""
            cursor.execute(query)
        else:
            query = """SELECT p.permission, arp.gameId FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public')
) AND (gameId IS NULL OR gameId = %s);"""
            cursor.execute(query, (gameId,))
        return fetchAllWithNames(cursor)

    @classmethod
    @dbConn()
    def listAll(self, cursor, db):
        """Lists all permission
        Returns:
            List[str]: list of permissions
        """
        query = """SELECT permission FROM permissions;"""
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        return result

def hasPermission(user: Union[str, UserModel, None], gameId: Union[str, None], permissions: Union[List[str], str]):
    """Returns list of permissions that user have from listed permissions

    Args:
        user (Union[str, UserModel, None]): user
        gameId (Union[str, None]): gameId
        permissions (str]): list of permission that you are looking for

    Returns:
        List[str]: list of permission from permission list that user has
    """
    if type(gameId) not in [str, int]:
        gameId = None
    userPerms = []
    if isinstance(user, str):
        user = UserModel.getById(user)
    if isinstance(permissions, str):
        permissions = [permissions]
    if user is None:
        userPerms = PermissionModel.listPublic(gameId=gameId)
    else:
        userPerms = user.listPermissions(gameId=gameId)
    uPermsFlat = []
    for perm in userPerms:
        uPermsFlat.append(perm["permission"])
    foundPerms = list(set(uPermsFlat).intersection(set(permissions)))
    return foundPerms
