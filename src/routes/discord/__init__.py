from .auth import Auth, TokenEndpoint, TestGetJWS

discordRoutes = [(Auth, '/auth'), (TokenEndpoint, '/token') ]
jwsForTesting = [(TestGetJWS, '/<userId>/')]
