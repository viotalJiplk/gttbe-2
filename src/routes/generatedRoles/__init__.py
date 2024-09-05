from .generatedRoles import GeneratedRoles, GeneratedRolesCreate, GeneratedRolePermissions, GeneratedRoleList

generatedRoleRoutes = [(GeneratedRolesCreate, '/create/'), (GeneratedRoles, '/<generatedRoleId>/'), (GeneratedRoleList, '/list/<gameId>/')]
