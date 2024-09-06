from shared.models import AssignedRolePermissionModel
from utils import ReturnableError
from utils import errorList

def getAssignedRolePermission(assignedRolePermissionId: str):
    """Gets assignedRolePermission from assignedRolePermissionId

    Args:
        assignedRolePermissionId (str): assignedRolePermissionId

    Raises:
        errorList.data.doesNotExist: assignedRolePermission does not exist

    Returns:
        AssignedRolePermissionModel: assignedRolePermission
    """
    assignedRolePermission = AssignedRolePermissionModel.getById(assignedRolePermissionId)
    if assignedRolePermission is None:
        raise errorList.data.doesNotExist
    return assignedRolePermission
