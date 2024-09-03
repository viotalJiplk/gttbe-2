from .generatedRoles import GeneratedRoles, GeneratedRolesCreate

generatedRoleRoutes = [(GeneratedRolesCreate, '/create/'), (GeneratedRoles, '/<generatedRoleId>/')]
