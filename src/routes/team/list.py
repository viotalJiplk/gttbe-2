from flask_restx import Resource
from shared.models import TeamModel
from utils import jwsProtected, hasPermissionDecorator, returnParser
from shared.utils import perms
from helper import getGame

class ListParticipatingTeam(Resource):
    @hasPermissionDecorator([perms.team.listParticipating, perms.team.listParticipatingDiscord], True)
    def get(self, gameId, withDiscord, authResult, permissions):
        """List teams currently able to participate in tournament

        Args:
            gameId (str): id of game
            withDiscord (bool): get discord info (for admins only)

        Returns:
            dict: list of teams
        """
        game = getGame(gameId)
        return TeamModel.listParticipatingTeams(game.gameId, perms.team.listParticipatingDiscord in permissions, withDiscord == 'true')
