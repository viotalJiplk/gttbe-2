from shared.models import RankModel
from utils import ReturnableError
from utils import errorList

def getRank(rankId: str):
    """Gets game from rankId

    Args:
        rankId (str): rankId

    Raises:
        errorList.data.doesNotExist: rank does not exist

    Returns:
        RankModel: rank
    """
    rank = RankModel.getById(rankId)
    if rank is None:
        raise errorList.data.doesNotExist
    return rank
