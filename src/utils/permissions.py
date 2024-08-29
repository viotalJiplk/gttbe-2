from functools import wraps
from flask_restful import request
from utils.error import handleReturnableError, ReturnableError
from utils.jws import getAuth, AuthResult
from utils.errorList import errorList
from shared.models.permission import hasPermission
from typing import Union, List
from utils.errorList import errorList

def hasPermissionDecorator(permissions: Union[List[str], str], detectGame=False):
    if isinstance(permissions, str):
        tmpPermissions = permissions
        permissions = []
        permissions.append(tmpPermissions)
    def wrapper(func):
        @wraps(func)
        @handleReturnableError
        def wrappedGetPerms(*args, **kwargs):
            result = {}
            gameId = None
            if detectGame:
                if 'gameId' in kwargs:
                    gameId = kwargs['gameId']
                else:
                    if 'data' in kwargs:
                        if 'game_id' in kwargs['data']:
                            gameId = kwargs['data']['game_id']
                        elif 'gameId' in kwargs['data']:
                            gameId = kwargs['data']['gameId']
                        else:
                            raise errorList.permission.missingId
                    else:
                        raise errorList.permission.missingId
            try:
                result = getAuth(request.headers)
            except ReturnableError as e:
                if e.message == "Missing Authorization header!":
                    result = AuthResult(None, None)
                    pass
                else:
                    raise
            foundPerms = hasPermission(result.userId, gameId, permissions)
            if len(foundPerms) < 1:
                raise errorList.permission.missingPermission
            return func(*args, **kwargs, authResult=result, permissions=foundPerms)
        return wrappedGetPerms
    return wrapper