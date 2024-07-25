from flask_restx import Resource
from models.team import TeamModel
from utils.jws import jwsProtected
from utils.role import getRole

class ListTeam(Resource):

    @jwsProtected(optional=True)
    def get(self, authResult, userId):
        """List teams user is currently in

        Args:
            userId (str): @me or id of user

        Returns:
            dict: list of teams
        """
        if userId == "@me":
            if authResult is None:
                return {"kind": "Auth", "msg": "You have to provide valid jws for @me."}, 401
            return TeamModel.listUsersTeams(authResult["userId"], True), 200
        else:
            return TeamModel.listUsersTeams(userId, False), 200

class ListParticipatingTeam(Resource):
    @jwsProtected(optional=True)
    @getRole(['admin','gameOrganizer'])
    def get(self, gameId, withDiscord, authResult, hasRole):
        """List teams currently able to participate in tornament

        Args:
            gameId (str): id of game
            withDiscord (bool): get discord info (for admins only)

        Returns:
            dict: list of teams
        """
        return TeamModel.listParticipatingTeams(gameId, hasRole, withDiscord == 'true')
