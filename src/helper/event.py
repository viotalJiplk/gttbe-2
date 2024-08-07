from shared.models.event import EventModel
from utils.error import ReturnableError
from utils.errorList import errorList

def getEvent(eventId: str):
    """Gets event from eventId

    Args:
        eventId (str): eventId

    Raises:
        ReturnableError: event does not exist

    Returns:
        EventModel: event
    """
    event = EventModel.getById(eventId)
    if event is None:
        raise errorList.data.doesNotExist
    return event
