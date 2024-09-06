from shared.models import AssignedRoleModel
from utils import ReturnableError
from utils import errorList

def getAssignedRole(assignedRoleId: str):
    """Gets assignedRole from assignedRoleId

    Args:
        assignedRoleId (str): assignedRoleId

    Raises:
        errorList.data.doesNotExist: assignedRole does not exist

    Returns:
        AssignedRoleModel: assignedRole
    """
    assignedRole = AssignedRoleModel.getById(assignedRoleId)
    if assignedRole is None:
        raise errorList.data.doesNotExist
    return assignedRole
