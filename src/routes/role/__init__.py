from routes.role.add import AddRole
from flask_restful import Resource, request

class RoleDescr(Resource):
    def get(self):
        return [
            {
                "add": "add",
                "url": "add/",
                "type": "private",
                "method": "POST",
                "descr": "Adds admin role to user."
            },
        ], 200

roleRoutes = [(RoleDescr, '/'), (AddRole, "/add")]