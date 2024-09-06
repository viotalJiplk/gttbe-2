from shared.models import StageModel
from utils import ReturnableError
from utils import errorList

def getStage(stageId: str):
    """Gets stage from stageId

    Args:
        stageId (str): stageId

    Raises:
        errorList.data.doesNotExist: stage does not exist

    Returns:
        stageModel: stage
    """
    stage = StageModel.getById(stageId)
    if stage is None:
        raise errorList.data.doesNotExist
    return stage
