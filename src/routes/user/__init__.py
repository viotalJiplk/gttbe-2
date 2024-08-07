from routes.user.user import UserEndpoint, UserExistsEndpoint, UserPermissions, ListTeam
from flask_restx import Resource

userRoutes = [(UserEndpoint, '/<uid>/'), (UserExistsEndpoint, '/exists/<uid>/'), (UserPermissions, '/<uid>/permissions/<gameId>'), (ListTeam, '/<userId>/listTeams/')]
