from flask_restful import Resource, request
from models.team import TeamModel
from utils.jws import jwsProtected

class ListTeam(Resource):

    @jwsProtected(optional=True)
    def get(self, authResult, userId):
        if userId == "@me":
            if authResult is None:
                return {"kind": "Auth", "msg": "You have to provide valid jws for @me."}, 401
            return TeamModel.listUsersTeams(authResult["userId"], True), 200
        elif userId == "participating":
            return TeamModel.listParticipatingTeams()
        else:
            return TeamModel.listUsersTeams(userId, False), 200

class ListParticipatingTeam(Resource):
    def get(self, gameId):
        return TeamModel.listParticipatingTeams(gameId)
