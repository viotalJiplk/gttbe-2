from .generatedRoles import GeneratedRoles, GeneratedRolesCreate, GeneratedRolePermissions

generatedRoleRoutes = [(GeneratedRolesCreate, '/create/'), (GeneratedRoles, '/<generatedRoleId>/'), (GeneratedRolePermissions, '/<generatedRoleId>/permissions/')]
