from functools import wraps
from models.role import RoleModel

def getRole(roleArray, optional=True):
    def wrapper(func, optional=True):
        @wraps(func)
        def wrapGetRole(*args, **kwargs):
            hasRole = False
            passProcessing = False
            if 'authResult' in kwargs:
                if optional:
                    passProcessing = True
                else:
                    return {"kind": "ROLE", "msg": "Missing GameId."}, 401
            gameId = ""
            if 'gameId' in kwargs:
                gameId = kwargs['gameId']
            else:
                if 'data' in kwargs:
                    if 'game_id' in kwargs['data']:
                        gameId = kwargs['data']['game_id']
                    else:
                        if optional:
                            passProcessing = True
                        else:
                            return {"kind": "ROLE", "msg": "Missing GameId."}, 401
                else:
                    if optional:
                        passProcessing = True
                    else:
                        return {"kind": "ROLE", "msg": "Missing payload."}, 401
            if not passProcessing:
                hasRole = RoleModel.hasRole(kwargs['authResult']['userId'], roleArray, gameId)
            return func(hasRole=hasRole, *args, **kwargs)
        return wrapGetRole
    return wrapper

def hasRoleWithErrMsg(userId, roles, gameId=None):
    if(RoleModel.hasRole(userId, roles, gameId)):
        return True
    else:
        return {"kind":"ROLE", "msg": "You dont have required role."}, 401