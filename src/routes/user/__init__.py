from .user import UserEndpoint, UserExistsEndpoint, UserPermissions, ListTeam, UserGeneratedRoles, UserAssignedRoles
from flask_restx import Resource

userRoutes = [(UserEndpoint, '/<userId>/'), (UserExistsEndpoint, '/<userId>/exists/'), (UserPermissions, '/<userId>/permissions/<gameId>'), (ListTeam, '/<userId>/teams/'), (UserGeneratedRoles, '/<userId>/generatedRoles/'), (UserAssignedRoles, '/<userId>/assignedRoles/')]
