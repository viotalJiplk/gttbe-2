from functools import wraps
from shared.models.role import RoleModel

def getRole(roleArray, optional=True):
    def wrapper(func):
        @wraps(func)
        def wrapGetRole(*args, **kwargs):
            hasRole = False
            passProcessing = False
            if 'authResult' not in kwargs or kwargs['authResult'] is None:
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
                    elif 'gameId' in kwargs['data']:
                        gameId = kwargs['data']['gameId']
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
            if not hasRole and not optional:
                return {"kind": "ROLE", "msg": "Inadequate role."}, 401
            return func(hasRole=hasRole, *args, **kwargs)
        return wrapGetRole
    return wrapper

def hasRoleWithErrMsg(userId, roles, gameId=None):
    if(RoleModel.hasRole(userId, roles, gameId)):
        return True
    else:
        return {"kind":"ROLE", "msg": "You dont have required role."}, 401
