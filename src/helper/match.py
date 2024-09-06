from shared.models import MatchModel
from utils import ReturnableError
from utils import errorList

def getMatch(matchId: str):
    """Gets match from matchId

    Args:
        matchId (str): matchId

    Raises:
        errorList.data.doesNotExist: match does not exist

    Returns:
        MatchModel: match
    """
    match = MatchModel.getById(matchId)
    if match is None:
        raise errorList.data.doesNotExist
    return match
