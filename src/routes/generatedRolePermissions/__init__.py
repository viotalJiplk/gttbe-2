from .generatedRolePermissions import GeneratedRolePermissions, GeneratedRolePermissionsCreate

generatedRolePermissionRoutes = [(GeneratedRolePermissions, '/<generatedRolePermissionId>/'), (GeneratedRolePermissionsCreate, '/create')]
