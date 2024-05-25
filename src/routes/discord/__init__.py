from routes.discord.auth import Auth, TokenEndpoint
from flask_restful import Resource, request

class DisDescr(Resource):
    def get(self):
        return [
            {
                "name": "auth",
                "url": "auth/",
                "type": "public",
                "method": "GET",
                "descr": "Generates discord api uri. You should add &redirect_uri=$uri$ at the end\
                so discord would redirect user to your client."
            },
            {
                "name": "get_jws",
                "url": "token/",
                "type": "public",
                "method": "POST",
                "descr": "Exchange OAuth code for jws."
            }
        ], 200

discordRoutes = [(DisDescr, '/'), (Auth, '/auth'), (TokenEndpoint, '/token') ]
