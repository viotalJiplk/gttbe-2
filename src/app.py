from flask import Flask, jsonify, request, abort
#from flask_cors import CORS
from flask_restful import Resource, Api
from utils.register_routes import register_routes
from config import production
from utils.logging import defaultLogger

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

if not production:
    register_routes(api, testRoutes, '/test', False)
    defaultLogger.warning("Test build DO NOT USE IN PRODUCTION!")

defaultLogger.info("Server started")

#app.run(port=5000)