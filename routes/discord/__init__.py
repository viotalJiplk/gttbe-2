from routes.discord.auth import Auth, Redirected
from routes.discord.tets import Test

discordRoutes = [(Auth, '/auth'), (Redirected, '/redirected'), (Test, '/test') ]