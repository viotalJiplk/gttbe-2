from flask_restx import Resource
from shared.models.team import TeamModel
from utils.jws import jwsProtected
from shared.utils.permissionList import perms
from utils.permissions import hasPermissionDecorator
from helper.game import getGame

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
