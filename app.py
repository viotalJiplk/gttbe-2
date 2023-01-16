from flask import Flask, jsonify, request, abort
#from flask_cors import CORS
from flask_restful import Resource, Api
from utils.register_routes import register_routes
import os

# ROUTES
from routes.discord import discordRoutes
from tests import testRoutes

app = Flask(__name__)
#CORS(app)

# if __name__ == "__main__":  
api = Api(app)

register_routes(api, discordRoutes, '/discord')

if(os.getenv("PROD") is None):
    register_routes(api, testRoutes, '/test')

#app.run(port=5000)