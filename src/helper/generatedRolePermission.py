from shared.models import GeneratedRolePermissionModel
from utils import ReturnableError
from utils import errorList

def getGeneratedRolePermission(generatedRolePermissionId: str):
    """Gets generatedRolePermission from generatedRolePermissionId

    Args:
        generatedRolePermissionId (str): generatedRolePermissionId

    Raises:
        errorList.data.doesNotExist: generatedRolePermission does not exist

    Returns:
        GeneratedRolePermissionModel: generatedRolePermission
    """
    generatedRolePermission = GeneratedRolePermissionModel.getById(generatedRolePermissionId)
    if generatedRolePermission is None:
        raise errorList.data.doesNotExist
    return generatedRolePermission
