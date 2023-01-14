from flask import Flask, jsonify, request, abort

from flask_restful import Resource, Api
from utils.register_routes import register_routes

# ROUTES
from routes.discord import discordRoutes
app = Flask(__name__)

# if __name__ == "__main__":   
api = Api(app)

register_routes(api, discordRoutes, '/discord')
#app.run(port=5000)5