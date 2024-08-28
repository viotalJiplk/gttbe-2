#!/usr/bin/env python3
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request, abort
#from flask_cors import CORS
#from flask_restful import Resource, Api
from flask_restx import Api, Resource, fields
from utils.register import registerRoutes
from shared.utils import config
from shared.utils import defaultLogger

# ROUTES
from routes.discord import discordRoutes, jwsForTesting
from routes.schools import schoolsRoutes
from routes.user import userRoutes
from routes.team import teamRoutes
from routes.games import gameRoutes
from routes.page import pageRoutes
from routes.events import eventRoutes
from routes.stage import stageRoutes
from routes.matches import matchRoutes
from tests import testRoutes
from json import JSONEncoder
app = Flask(__name__)

class nonAsciiJSONEncoder(JSONEncoder):
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        super(NonASCIIJSONEncoder, self).__init__(**kwargs)
app.json_encoder = nonAsciiJSONEncoder


#CORS(app)
docs = False
if not config.production:
    docs = '/docs'

api = Api(app, version='2.0', title='gtt-be',
          description='Gt tournament information system API',
          doc=docs,
          prefix='/backend'
          )
api.json_encoder = nonAsciiJSONEncoder

registerRoutes(api.namespace('discord', description="login"), discordRoutes)
registerRoutes(api.namespace('schools', description='schools'), schoolsRoutes)
registerRoutes(api.namespace('user', description='user'), userRoutes)
registerRoutes(api.namespace('team', description='team'), teamRoutes)
registerRoutes(api.namespace('game', description='game'), gameRoutes)
registerRoutes(api.namespace('page', description='page'), pageRoutes)
registerRoutes(api.namespace('event', description='event'), eventRoutes)
registerRoutes(api.namespace('stage', description='stage'), stageRoutes)
registerRoutes(api.namespace('match', description='match'), matchRoutes)

if not config.production:
    registerRoutes(api.namespace('test', description='for backend development'), testRoutes)
    registerRoutes(api.namespace('jwsfortestingonly', description='for testing'), jwsForTesting)
    defaultLogger.warning("Test build NEVER EVER USE THIS IN PRODUCTION!")

defaultLogger.info("Server started")
if __name__ == "__main__":
    app.run(port=5000)
