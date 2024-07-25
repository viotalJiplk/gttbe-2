from flask import Flask, jsonify, request, abort
#from flask_cors import CORS
#from flask_restful import Resource, Api
from flask_restx import Api, Resource, fields
from utils.register_routes import register_routes
from utils.config import config
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
#CORS(app)
docs = False
if not config.production:
    docs = '/docs'
# if __name__ == "__main__":
api = Api(app, version='2.0', title='gtt-be',
          description='Gt tournament information system API',
          doc=docs,
          prefix='/backend'
          )

register_routes(api.namespace('discord', description="login"), discordRoutes)
register_routes(api.namespace('schools', description='schools'), schoolsRoutes)
register_routes(api.namespace('user', description='user'), userRoutes)
register_routes(api.namespace('team', description='team'), teamRoutes)
register_routes(api.namespace('game', description='game'), gameRoutes)
register_routes(api.namespace('page', description='page'), pageRoutes)
register_routes(api.namespace('event', description='event'), eventRoutes)
register_routes(api.namespace('role', description='role'), roleRoutes)
register_routes(api.namespace('stage', description='stage'), stageRoutes)
register_routes(api.namespace('match', description='match'), matchRoutes)

if not config.production:
    register_routes(api.namespace('test', description='for backend development'), testRoutes)
    defaultLogger.warning("Test build DO NOT USE IN PRODUCTION!")

defaultLogger.info("Server started")

#app.run(port=5000)
