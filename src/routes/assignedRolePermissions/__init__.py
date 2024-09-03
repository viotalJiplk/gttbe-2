from .assignedRolePermissions import AssignedRolePermissions, AssignedRolePermissionsCreate

assignedRolePermissionRoutes = [(AssignedRolePermissionsCreate, '/create'), (AssignedRolePermissions, '/<assignedRolePermissionId>/')]
