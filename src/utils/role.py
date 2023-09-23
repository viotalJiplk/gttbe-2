from functools import wraps
from models.role import RoleModel

def getRole(roleArray):
    def wrapper(func):
        @wraps(func)
        def wrapGetRole(*args, **kwargs):
            if kwargs['data']['game_id'] is None:
                return {"kind": "ROLE", "msg": "Missing GameId."}, 401
            hasRole = RoleModel.hasRole(kwargs['authResult']['userId'], kwargs['data']['game_id'], roleArray)
            return func(hasRole=hasRole, *args, **kwargs)
        return wrapGetRole
    return wrapper

def hasRoleWithErrMsg(userId, roles, gameId=None):
    if(RoleModel.hasRole(userId, roles, gameId)):
        return True
    else:
        return {"kind":"ROLE", "msg": "You dont have required role."}, 401