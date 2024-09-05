from .assignedRoles import AssignedRoles, AssignedRolesCreate, AssignedRolePermissions, AssignedRoleList

assignedRoleRoutes = [(AssignedRolesCreate, '/create'), (AssignedRoles, '/<assignedRoleId>/'), (AssignedRolePermissions, '/<assignedRoleId>/permissions/'), (AssignedRoleList, '/listAll/')]
