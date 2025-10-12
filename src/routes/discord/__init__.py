from .auth import Auth, TokenEndpoint, TestGetJWS
from .external import PublicKeys

discordRoutes = [(Auth, '/auth'), (TokenEndpoint, '/token') ]
jwsForTesting = [(TestGetJWS, '/<userId>/')]
externalLogin = [(PublicKeys, '/certs')]
