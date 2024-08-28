from flask_restx import Resource
from shared.models.team import TeamModel
from shared.models.game import GameModel
from utils.jws import AuthResult
from utils.others import postJson
from shared.models.user import UserModel
from shared.utils.permissionList import perms
from helper.game import getGame
from helper.user import getUser
from utils.errorList import errorList
from utils.permissions import hasPermissionDecorator
from typing import List
from shared.utils import DatabaseError

class createTeam(Resource):

    @postJson
    @hasPermissionDecorator(perms.team.create, True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates team

        Args:

        Returns:
            dict: teamId
        """
        if("game_id" not in data or "name" not in data):
            raise errorList.team.missingGameIdOrName
        game = getGame(data["game_id"])
        if not game.canBeRegistered():
           raise errorList.team.registrationNotOpened
        if("nick" not in data or "rank" not in data or "max_rank" not in data):
            raise errorList.team.invalidPayload
        user = getUser(authResult)
        if user is None:
            raise errorList.data.doesNotExist
        if not user.canRegister():
           raise errorList.user.couldNotRegister
        try:
            team = TeamModel.create(name=data["name"], gameId=data["game_id"], userId=authResult.userId, nick=data["nick"], rank=data["rank"], maxRank=data["max_rank"])
        except DatabaseError as e:
            if e.message == "Already registered for game":
                raise errorList.team.alreadyRegistered
            elif e.message == "No space for this role in this team":
                raise errorList.team.noSpaceLeft
            raise
        return team.toDict(), 200
