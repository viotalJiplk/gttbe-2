from functools import wraps
from models.role import RoleModel

def getRole(roleArray):
    def wrapper(func, optional=True):
        @wraps(func)
        def wrapGetRole(*args, **kwargs):
            hasRole = False
            passPrcessing = False
            if kwargs['authResult'] is None:
                if optional:
                    passPrcessing = True
                else:
                    return {"kind": "ROLE", "msg": "Missing GameId."}, 401
            gameId = ""
            if kwargs['gameId'] is not None:
                gameId = kwargs['gameId']
            else:
                if kwargs['data'] is not None:
                    if kwargs['data']['game_id'] is not None:
                        gameId = kwargs['data']['game_id']
                    else:
                        if optional:
                            passPrcessing = True
                        else:
                            return {"kind": "ROLE", "msg": "Missing GameId."}, 401
                else:
                    if optional:
                        passPrcessing = True
                    else:
                        return {"kind": "ROLE", "msg": "Missing payload."}, 401
            if not passPrcessing:
                hasRole = RoleModel.hasRole(kwargs['authResult']['userId'], roleArray, gameId)
            return func(hasRole=hasRole, *args, **kwargs)
        return wrapGetRole
    return wrapper

def hasRoleWithErrMsg(userId, roles, gameId=None):
    if(RoleModel.hasRole(userId, roles, gameId)):
        return True
    else:
        return {"kind":"ROLE", "msg": "You dont have required role."}, 401