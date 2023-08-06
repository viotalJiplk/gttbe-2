from flask import Flask, jsonify, request, abort
#from flask_cors import CORS
from flask_restful import Resource, Api
from utils.register_routes import register_routes
import os

# ROUTES
from routes.discord import discordRoutes
from routes.schools import schoolsRoutes
from routes.user import userRoutes
from routes.team import teamRoutes
from routes.games import gameRoutes
from tests import testRoutes

app = Flask(__name__)
#CORS(app)

# if __name__ == "__main__":  
api = Api(app)

register_routes(api, discordRoutes, '/discord')
register_routes(api, schoolsRoutes, '/schools')
register_routes(api, userRoutes, '/user')
register_routes(api, teamRoutes, '/team')
register_routes(api, gameRoutes, '/game')

if(os.getenv("PROD") is None):
    register_routes(api, testRoutes, '/test')
    print("Test build DO NOT USE IN PRODUCTION!")
else:
    if(os.getenv("PROD")=="no"):
        register_routes(api, testRoutes, '/test')
        print("Test build DO NOT USE IN PRODUCTION!")

#app.run(port=5000)