from flask_restful import Resource, request
from models.team import TeamModel
from utils.jws import jwsProtected

class ListTeam(Resource):

    @jwsProtected(optional=True)
    def get(self, authResult, userId):
        if userId == "@me":
            if authResult is None:
                return {"kind": "Auth", "msg": "You have to provide valid jws for @me."}, 401
            return TeamModel.listUsersTeams(authResult["userId"]), 200
        else:
            return TeamModel.listUsersTeams(userId), 200