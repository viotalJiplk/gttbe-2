from shared.models.team import TeamModel
from utils.error import ReturnableError
from utils.errorList import errorList

def getTeam(teamId: str):
    """Gets team from teamId

    Args:
        teamId (str): teamId

    Raises:
        ReturnableError: team does not exist

    Returns:
        TeamModel: team
    """
    team = TeamModel.getById(teamId)
    if team is None:
        raise errorList.data.doesNotExist
    return team
