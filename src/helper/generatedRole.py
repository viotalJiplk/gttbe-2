from shared.models import GeneratedRoleModel
from utils import ReturnableError
from utils import errorList

def getGeneratedRole(generatedRoleId: str):
    """Gets generatedRole from generatedRoleId

    Args:
        generatedRoleId (str): generatedRoleId

    Raises:
        errorList.data.doesNotExist: generatedRole does not exist

    Returns:
        GeneratedRoleModel: generatedRole
    """
    generatedRole = GeneratedRoleModel.getById(generatedRoleId)
    if generatedRole is None:
        raise errorList.data.doesNotExist
    return generatedRole
