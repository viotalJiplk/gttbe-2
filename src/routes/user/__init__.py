from routes.user.user import UserEndpoint, UserExistsEndpoint
from flask_restful import Resource, request

class UserDescr(Resource):
    def get(self):
        return [
            {
                "name": "userinfo",
                "url": "<userId>/",
                "type": "public",
                "method": "GET",
                "descr": "Basic userinfo for non admin accounts only <userId> = @me is allowed."
            },
            {
                "name": "delete_user",
                "url": "<userId>/",
                "type": "public",
                "method": "DELETE",
                "descr": "Deletes user from database. You have to leave all teams before attempting this."
            }
        ], 200

userRoutes = [(UserDescr, '/'), (UserEndpoint, '/<uid>/'), (UserExistsEndpoint, '/exists/<uid>/')]
