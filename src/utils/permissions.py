from functools import wraps
from flask_restful import request
from .error import handleReturnableError, ReturnableError
from .jws import getAuth, AuthResult
from .errorListFile import errorList
from shared.models.permission import hasPermission
from typing import Union, List
from .nsForDecorators import blankNs
from .others import returnError

def hasPermissionDecorator(permissions: Union[List[str], str], detectGame=False):
    """decorator that test if user has required permission\

    Args:
        permissions (Union[List[str], str]): wanted permissions
        detectGame (bool, optional): Are this permissions game sensitive. Defaults to False.

    Raises:
        errorList.permission.missingId: Missing gameId
        errorList.permission.missingPermission: Missing permission
    """
    errors = [errorList.jws.invalidToken, errorList.jws.InvalidSignature, errorList.jws.expired, errorList.jws.untrusted, errorList.jws.missingUserId, errorList.permission.missingPermission, errorList.jws.malformedToken, errorList.jws.issuedInFuture, errorList.jws.wrongAudience]
    if detectGame:
        errors.append(errorList.permission.missingId)
    if isinstance(permissions, str):
        tmpPermissions = permissions
        permissions = []
        permissions.append(tmpPermissions)
    def wrapper(func):
        @wraps(func)
        @blankNs.doc(security="jws")
        @returnError(errors)
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
                if "backend" not in result.audience:
                    raise errorList.jws.wrongAudience
            except ReturnableError as e:
                if e.message == "Missing Authorization header!":
                    result = AuthResult(None, None, None, None, None, None, None, None, None)
                    pass
                else:
                    raise
            foundPerms = hasPermission(result.userId, gameId, permissions)
            if len(foundPerms) < 1:
                raise errorList.permission.missingPermission
            return func(*args, **kwargs, authResult=result, permissions=foundPerms)
        return wrappedGetPerms
    return wrapper
