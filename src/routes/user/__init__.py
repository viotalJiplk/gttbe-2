from .user import UserEndpoint, UserExistsEndpoint, UserPermissions, ListTeam
from flask_restx import Resource

userRoutes = [(UserEndpoint, '/<uid>/'), (UserExistsEndpoint, '/<uid>/exists/'), (UserPermissions, '/<uid>/permissions/<gameId>'), (ListTeam, '/<userId>/teams/')]
