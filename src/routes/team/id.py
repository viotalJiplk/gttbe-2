from flask_restx import Resource, fields
from shared.models import TeamModel
from utils import jwsProtected, AuthResult, postJsonParse, handleReturnableError, errorList, returnParser
from shared.models import hasPermission
from helper import getTeam, getUser, getGame
from shared.utils import perms, DatabaseError

accessibleAttributes = {
    "name": [str],
    "gameId": [int],
    "teamId": [int]
}

class Team(Resource):
    # @returnParser("_team.get",{
    #         "name": [str],
    #         "teamId": [int],
    #         "gameId": [int],
    #         "Players": {
    #             'userId': [str],
    #             'nick': [str],
    #             'generatedRoleId': [int]
    #     }}, 200, False, False)
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, teamId: str):
        """Gets team

        Args:
            teamId (str): id of team

        Returns:
            dict: info about team
        """
        user = getUser(authResult)
        team = getTeam(teamId)
        permission = hasPermission(user, team.gameId, perms.team.read)
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        players = team.getPlayers()
        return {
            "name": team.name,
            "teamId": team.teamId,
            "gameId": team.gameId,
            "Players": players
        }, 200


class TeamJoinstring(Resource):
    @returnParser({"joinString": [str]}, 200, False, False)
    @handleReturnableError
    @jwsProtected(optional=True)
    def get(self, authResult: AuthResult, teamId: str):
        """Gets team joinString
            Captain only

        Args:
            teamId (str): id of team

        Returns:
            dict: joinString
        """
        user = getUser(authResult)
        team = getTeam(teamId)
        permission = hasPermission(user, team.gameId, [perms.team.generateJoinString, perms.team.generateJoinStringMyTeam])
        if len(permission) < 1:
            raise errorList.permission.missingPermission
        joinString = team.generateJoinString()
        if joinString is None:
            raise errorList.data.doesNotExist
        return {"joinString": joinString}, 200


class Join(Resource):

    @handleReturnableError
    @jwsProtected(optional=True)
    @returnParser({"teamId": [int]}, 200, False, False)
    @postJsonParse({"nick":[str], "rank": [int], "max_rank": [int], "generatedRoleId": [int]})
    def post(self, authResult: AuthResult, teamId: str, data, joinString: str):
        """Joins team

        Args:
            teamId (str): id of team
            joinString (str): joinString of team

        Returns:
            dict: teamId
        """
        team = getTeam(teamId)
        user = getUser(authResult)
        game = getGame(team.gameId)
        if game == None:
            raise errorList.data.doesNotExist
        if not game.canBeRegistered():
            raise errorList.team.registrationNotOpened

        permission = hasPermission(user, team.gameId, [perms.team.join])
        if len(permission) < 1:
            raise errorList.permission.missingPermission

        if(team.joinString != joinString):
            raise errorList.team.wrongJoinString
        if user is None:
            raise errorList.data.doesNotExist
        if not user.canRegister():
            raise errorList.user.couldNotRegister
        try:
            team.join(userId=authResult.userId, nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"], generatedRoleId=data["generatedRoleId"])
        except DatabaseError as e:
            if e.message == "Already registered for game.":
                raise errorList.team.alreadyRegistered
            elif e.message == "No space for this role in this team.":
                raise errorList.team.noSpaceLeft
            raise
        return {"teamId":team.teamId}, 200


class Kick(Resource):
    @returnParser({"teamId": [int]}, 200, False, False)
    @handleReturnableError
    @jwsProtected(optional=True)
    def delete(self, authResult: AuthResult, teamId: str, userId: str):
        """Kicks user out of team

        Args:
            teamId (str): id of team
            userId (str): @me (or id of user captain and admin only)

        Returns:
            dict: teamId
        """
        team = getTeam(teamId)
        user = getUser(authResult)
        permission = hasPermission(user, team.gameId, [perms.team.kickTeam, perms.team.leave, perms.team.kick])
        if len(permission) < 1:
            raise errorList.permission.missingPermission

        if perms.team.kick in permission:
            if not team.leave(userId):
                raise errorList.team.userNotPartOfTeam
        elif perms.team.kickTeam in permission and team.getUsersRole(authResult.userId) == "Captain":
            if not team.leave(userId):
                raise errorList.team.userNotPartOfTeam
        elif perms.team.leave in permission and userId == "@me":
            if not team.leave(userId=authResult.userId):
                raise errorList.team.userNotPartOfTeam
        else:
            raise errorList.permission.missingPermission
        return {"teamId":team.teamId}, 200
