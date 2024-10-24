from shared.models import SponsorModel
from utils import ReturnableError
from utils import errorList

def getSponsor(sponsorId: str):
    """Gets s from sponsorId

    Args:
        sponsorId (str): sponsorId

    Raises:
        errorList.data.doesNotExist: sponsor does not exist

    Returns:
        SponsorModel: sponsor
    """
    sponsor = SponsorModel.getById(sponsorId)
    if sponsor is None:
        raise errorList.data.doesNotExist
    return sponsor
