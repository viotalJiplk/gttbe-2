from shared.models import UserRoleModel
from utils import ReturnableError
from utils import errorList

def getUserRole(userRolesId: str):
    """Gets userRoles from userRolesId

    Args:
        userRolesId (str): userRolesId

    Raises:
        ReturnableError: userRoles does not exist

    Returns:
        UserRolesModel: userRoles
    """
    userRoles = UserRoleModel.getById(userRolesId)
    if userRoles is None:
        raise errorList.data.doesNotExist
    return userRoles
