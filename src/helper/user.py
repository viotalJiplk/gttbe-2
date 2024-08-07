from shared.models.user import UserModel
from utils.jws import AuthResult
from utils.error import ReturnableError
from typing import Union
from utils.errorList import errorList

def getUser(authResult: Union[AuthResult, None]):
    """Returns user from AuthResult

    Args:
        authResult (Union[AuthResult, None]): authResult

    Raises:
        ReturnableError: If user does not exist

    Returns:
        Union[UserModel, None]: result
    """
    user = None
    if authResult is not None:
        user = UserModel.getById(authResult.userId)
        if user is None:
            raise errorList.data.doesNotExist
    return user
