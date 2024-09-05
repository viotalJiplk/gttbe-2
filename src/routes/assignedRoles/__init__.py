from .assignedRoles import AssignedRoles, AssignedRolesCreate, AssignedRolePermissions

assignedRoleRoutes = [(AssignedRolesCreate, '/create'), (AssignedRoles, '/<assignedRoleId>/'), (AssignedRolePermissions, '/<assignedRoleId>/permissions/')]
