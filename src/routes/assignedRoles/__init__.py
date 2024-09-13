from .assignedRoles import AssignedRoles, AssignedRolesCreate, AssignedRolePermissionList, AssignedRoleList

assignedRoleRoutes = [(AssignedRolesCreate, '/create'), (AssignedRoles, '/<assignedRoleId>/'), (AssignedRolePermissionList, '/<assignedRoleId>/permissions/'), (AssignedRoleList, '/listAll/')]
