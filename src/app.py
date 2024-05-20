from flask import Flask, jsonify, request, abort
#from flask_cors import CORS
from flask_restful import Resource, Api
from utils.register_routes import register_routes
import os
from utils.logging import getLogger

# ROUTES
from routes.discord import discordRoutes
from routes.schools import schoolsRoutes
from routes.user import userRoutes
from routes.team import teamRoutes
from routes.games import gameRoutes
from routes.page import pageRoutes
from routes.events import eventRoutes
from routes.role import roleRoutes
from routes.stage import stageRoutes
from routes.matches import matchRoutes
from tests import testRoutes

mainLogger = getLogger("app")

app = Flask(__name__)
#CORS(app)7

# if __name__ == "__main__":  
api = Api(app)

register_routes(api, discordRoutes, '/discord')
register_routes(api, schoolsRoutes, '/schools')
register_routes(api, userRoutes, '/user')
register_routes(api, teamRoutes, '/team')
register_routes(api, gameRoutes, '/game')
register_routes(api, pageRoutes, '/page')
register_routes(api, eventRoutes, '/event')
register_routes(api, roleRoutes, '/role')
register_routes(api, stageRoutes, '/stage')
register_routes(api, matchRoutes, '/match')

if(os.getenv("PROD") is None):
    register_routes(api, testRoutes, '/test', False)
    mainLogger.warning("Test build DO NOT USE IN PRODUCTION!")
else:
    if(os.getenv("PROD")=="no"):
        register_routes(api, testRoutes, '/test', False)
        mainLogger.warning("Test build DO NOT USE IN PRODUCTION!")

#app.run(port=5000)