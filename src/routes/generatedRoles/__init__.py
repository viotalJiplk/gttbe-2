from .generatedRoles import GeneratedRoles, GeneratedRolesCreate, GeneratedRolePermissionList, GeneratedRoleList

generatedRoleRoutes = [(GeneratedRolesCreate, '/create/'), (GeneratedRoles, '/<generatedRoleId>/'), (GeneratedRoleList, '/list/<gameId>/'), (GeneratedRolePermissionList, '/<generatedRoleId>/permissions/')]
