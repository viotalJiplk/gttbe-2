from shared.models.match import MatchModel
from utils.error import ReturnableError
from utils.errorList import errorList

def getMatch(matchId: str):
    """Gets match from matchId

    Args:
        matchId (str): matchId

    Raises:
        ReturnableError: match does not exist

    Returns:
        MatchModel: match
    """
    match = MatchModel.getById(matchId)
    if match is None:
        raise errorList.data.doesNotExist
    return match
