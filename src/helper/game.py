from shared.models.game import GameModel
from utils.error import ReturnableError
from utils.errorList import errorList

def getGame(gameId: str):
    """Gets game from gameId

    Args:
        gameId (str): gameId

    Raises:
        ReturnableError: game does not exist

    Returns:
        GameModel: game
    """
    game = GameModel.getById(gameId)
    if game is None:
        raise errorList.data.doesNotExist
    return game
