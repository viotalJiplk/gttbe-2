from mysql.connector.errors import IntegrityError
from ..utils import ObjectDbSync
from ..utils import dbConn
from typing import Union, List
from ..models.user import UserModel

class PermissionModel(ObjectDbSync):
    tableName = "permissions"
    tableId = "permission"

    def __init__(self, permission):
        self.permission = permission
        super().__init__()


    @classmethod
    @dbConn()
    def create(cls, permission, cursor, db):
        query = f"INSERT INTO `{cls.tableName}` (permission) VALUES (%s)"
        try:
            cursor.execute(query, (permission,))
        except IntegrityError as e:
            raise ValueError("This permission already exists")
        return cls(permission)

    @classmethod
    @dbConn()
    def listPublic(cls, gameId, cursor, db):
        if(gameId is None):
            query = """SELECT p.permission FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public') AND gameId IS NULL
);"""
            cursor.execute(query)
        else:
            query = """SELECT p.permission FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public') AND (gameId IS NULL OR gameId = %s)
);"""
            cursor.execute(query, (gameId,))
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
    userPerms = []
    if isinstance(user, str):
        user = UserModel.getById(user)
    if isinstance(permissions, str):
        permissions = [permissions]
    if user is None:
        userPerms = PermissionModel.listPublic(gameId=gameId)
    else:
        userPerms = user.listPermissions(gameId=gameId)
    foundPerms = list(set(userPerms).intersection(set(permissions)))
    return foundPerms