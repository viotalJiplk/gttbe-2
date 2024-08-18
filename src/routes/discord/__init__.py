from .auth import Auth, TokenEndpoint, TestGetJWS
from flask_restx import Resource

discordRoutes = [(Auth, '/auth'), (TokenEndpoint, '/token') ]
jwsForTesting = [(TestGetJWS, '/<userId>/')]
