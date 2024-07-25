from routes.discord.auth import Auth, TokenEndpoint
from flask_restx import Resource
from routes.matches.matches import Matches, MatchCreate

matchRoutes = [(MatchCreate, '/create/'), (Matches, '/<matchId>/')]
