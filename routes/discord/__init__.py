from routes.discord.auth import Auth, TokenEndpoint

discordRoutes = [(Auth, '/auth'), (TokenEndpoint, '/token') ]