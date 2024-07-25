from routes.user.user import UserEndpoint, UserExistsEndpoint
from flask_restx import Resource

userRoutes = [(UserEndpoint, '/<uid>/'), (UserExistsEndpoint, '/exists/<uid>/')]
