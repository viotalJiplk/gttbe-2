from utils.db import fetchAllWithNames, dbConn

class RoleModel:
    def __init__(self, userId, gameId, role):        
        self.userId = userId
        self.gameId = gameId
        self.role = role

    @classmethod
    @dbConn()
    def create(cls,userId, gameId, role, cursor, db):
        query = "INSERT INTO `roles` (`userId`, `gameId`, `role`) VALUES (%s, %s, %s)"
        cursor.execute(query, (userId, gameId, role))
        return cls(userId=userId, gameId=gameId, role=role)

    @classmethod
    @dbConn()
    def hasRole(cls, userId, roles, gameId = None, cursor = None, db = None):
        query = "SELECT `role` FROM `roles` WHERE `userId`=%s"
        if gameId is not None:
            query += "AND `gameId`=%s"
            cursor.execute(query, (userId, gameId))
        else:
            cursor.execute(query, (userId,))
        userRoles = fetchAllWithNames(cursor)
        if userRoles == None:
            return False
        for userRole in userRoles:
            if userRole["role"] in roles:
                return True
        return False
    
    @classmethod
    @dbConn()
    def listRole(cls, userId):
        query = "SELECT `role` FROM `roles` WHERE `userId`=%s"
        cursor.execute(query, (userId, ))
        return False