#!/usr/bin/env python3
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, abort, Response
from flask_cors import CORS
#from flask_restful import Resource, Api
from flask_restx import Api, Resource, fields
from utils import registerRoutes
from shared.utils import config
from shared.utils import defaultLogger
from werkzeug.middleware.proxy_fix import ProxyFix

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
from routes.assignedRoles import assignedRoleRoutes
from routes.assignedRolePermissions import assignedRolePermissionRoutes
from routes.generatedRoles import generatedRoleRoutes
from routes.generatedRolePermissions import generatedRolePermissionRoutes
from routes.userRoles import userRolesRoutes
from routes.permissions import permissionsRoutes
from tests import testRoutes
from routes.file import fileRoutes
from routes.ranks import rankRoutes
from routes.sponsors import sponsorRoutes


app = Flask(import_name=__name__)

CORS(app)
docs = False
if not config.production:
    docs = '/'

authorizations = {
    "jws": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

if "https://" in config.selfref.root_url:
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)


api = Api(app, version='2.0', title='gtt-be',
          description='Gt tournament information system API',
          doc=docs,
          prefix='/backend',
          authorizations=authorizations
          )

if not config.production:
    registerRoutes(api.namespace('test', description='for backend development'), testRoutes)
    registerRoutes(api.namespace('jwsfortestingonly', description='for testing'), jwsForTesting)
    defaultLogger.warning("Test build NEVER EVER USE THIS IN PRODUCTION!")

registerRoutes(api.namespace('discord', description="login"), discordRoutes)
registerRoutes(api.namespace('school', description='schools'), schoolsRoutes)
registerRoutes(api.namespace('user', description='user'), userRoutes)
registerRoutes(api.namespace('team', description='team'), teamRoutes)
registerRoutes(api.namespace('game', description='game'), gameRoutes)
registerRoutes(api.namespace('page', description='page'), pageRoutes)
registerRoutes(api.namespace('event', description='event'), eventRoutes)
registerRoutes(api.namespace('stage', description='stage'), stageRoutes)
registerRoutes(api.namespace('match', description='match'), matchRoutes)
registerRoutes(api.namespace('assignedRole', description='assignedRole'), assignedRoleRoutes)
registerRoutes(api.namespace('assignedRolePermission', description='assignedRolePermission'), assignedRolePermissionRoutes)
registerRoutes(api.namespace('generatedRole', description='generatedRole'), generatedRoleRoutes)
registerRoutes(api.namespace('generatedRolePermission', description='generatedRolePermission'), generatedRolePermissionRoutes)
registerRoutes(api.namespace('userRole', description='userRole'), userRolesRoutes)
registerRoutes(api.namespace('permission', description='permissions'), permissionsRoutes)
registerRoutes(api.namespace('file', description='files'), fileRoutes)
registerRoutes(api.namespace('rank', description='ranks'), rankRoutes)
registerRoutes(api.namespace('sponsor', description='sponsors'), sponsorRoutes)

defaultLogger.info("Server started")
if __name__ == "__main__":
    app.run(port=5000)
