from .assignedRoles import AssignedRoles, AssignedRolesCreate

assignedRoleRoutes = [(AssignedRolesCreate, '/create'), (AssignedRoles, '/<assignedRoleId>/')]
