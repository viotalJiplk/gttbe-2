from routes.discord.auth import Auth, TokenEndpoint
from flask_restx import Resource

discordRoutes = [(Auth, '/auth'), (TokenEndpoint, '/token') ]
