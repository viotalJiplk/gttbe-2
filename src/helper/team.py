from shared.models import TeamModel
from utils import ReturnableError
from utils import errorList

def getTeam(teamId: str):
    """Gets team from teamId

    Args:
        teamId (str): teamId

    Raises:
        errorList.data.doesNotExist: team does not exist

    Returns:
        TeamModel: team
    """
    team = TeamModel.getById(teamId)
    if team is None:
        raise errorList.data.doesNotExist
    return team
