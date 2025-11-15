from flask_restx import Resource
from shared.models import TeamModel
from utils import jwsProtected, hasPermissionDecorator, returnParser
from shared.utils import perms
from helper import getGame

class ListParticipatingTeamsWithPlayers(Resource):
    @hasPermissionDecorator(perms.team.listParticipating, True)
    def get(self, gameId, authResult, permissions):
        """List teams currently able to participate in tournament

        Args:
            gameId (str): id of game
            withDiscord (bool): get discord info (for admins only)

        Returns:
            dict: list of teams
        """
        game = getGame(gameId)
        return TeamModel.listParticipatingTeamsWithPlayers(game.gameId)

class ListParticipatingTeamsWithPlayersAdmin(Resource):
    @hasPermissionDecorator(perms.team.listParticipatingAdmin, True)
    def get(self, gameId, withDiscord, authResult, permissions):
        """List teams currently able to participate in tournament with admin info

        Args:
            gameId (str): id of game
            withDiscord (bool): get discord info (could be slow)

        Returns:
            dict: list of teams
        """
        game = getGame(gameId)
        return TeamModel.listParticipatingTeamsWithPlayersAdmin(game.gameId, withDiscord == "true")
