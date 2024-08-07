from shared.models.stage import StageModel
from utils.error import ReturnableError
from utils.errorList import errorList

def getStage(stageId: str):
    """Gets stage from stageId

    Args:
        stageId (str): stageId

    Raises:
        ReturnableError: stage does not exist

    Returns:
        stageModel: stage
    """
    stage = StageModel.getById(stageId)
    if stage is None:
        raise errorList.data.doesNotExist
    return stage
