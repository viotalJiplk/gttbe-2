from .userRoles import UserRoles, UserRolesCreate

userRolesRoutes = [(UserRoles, '/<userRoleId>/'), (UserRolesCreate, '/create')]
