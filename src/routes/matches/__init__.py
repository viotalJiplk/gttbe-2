from routes.discord.auth import Auth, TokenEndpoint
from flask_restful import Resource, request
from routes.matches.matches import Matches, MatchCreate

class MatchDescr(Resource):
    def get(self):
        return [
            {
                "name": "list",
                "url": "list/",
                "type": "public",
                "method": "GET",
                "descr": "Gets all matches."
            }
        ], 200

matchRoutes = [(MatchDescr, '/'), (MatchCreate, '/create/'), (Matches, '/<matchId>/')]
