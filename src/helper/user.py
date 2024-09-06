from shared.models import UserModel
from utils import AuthResult
from utils import ReturnableError
from typing import Union
from utils import errorList

def getUser(authResult: Union[AuthResult, None]):
    """Returns user from AuthResult

    Args:
        authResult (Union[AuthResult, None]): authResult

    Raises:
        errorList.data.doesNotExist: user does not exist

    Returns:
        Union[UserModel, None]: result
    """
    user = None
    if authResult is not None:
        user = UserModel.getById(authResult.userId)
        if user is None:
            raise errorList.data.doesNotExist
    return user
