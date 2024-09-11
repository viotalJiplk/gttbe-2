from flask_restx import Resource
from shared.models import TeamModel
from utils import AuthResult, postJsonParse, errorList, hasPermissionDecorator, returnParser, returnError
from shared.utils import perms, DatabaseError
from helper import getGame, getUser
from typing import List

createAttributes = {
    "gameId": [int],
    "name": [str],
    "nick": [str],
    "rank": [int],
    "maxRank": [int],
}
returnableAttributes =  {
    "teamId": [int],
    "gameId": [int],
    "name": [str],
    "joinString": [str, type(None)]
}

class createTeam(Resource):
    @returnParser(returnableAttributes, 201, False, False)
    @postJsonParse(createAttributes)
    @returnError([errorList.data.doesNotExist, errorList.team.registrationNotOpened, errorList.user.couldNotRegister, errorList.team.alreadyRegistered, errorList.team.noSpaceLeft])
    @hasPermissionDecorator(perms.team.create, True)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        """Creates team

        Args:

        Returns:
            dict: teamId
        """
        game = getGame(data["gameId"])
        if not game.canBeRegistered():
           raise errorList.team.registrationNotOpened
        user = getUser(authResult)
        if user is None:
            raise errorList.data.doesNotExist
        if not user.canRegister():
           raise errorList.user.couldNotRegister
        try:
            team = TeamModel.create(name=data["name"], gameId=data["gameId"], userId=authResult.userId, nick=data["nick"], rank=data["rank"], maxRank=data["maxRank"])
        except DatabaseError as e:
            if e.message == "Already registered for game.":
                raise errorList.team.alreadyRegistered
            elif e.message == "No space for this role in this team.":
                raise errorList.team.noSpaceLeft
            raise
        return team.toDict(), 201
