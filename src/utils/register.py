from flask import Flask
from click import Command
from flask_restx import Api
from typing import List

def registerRoutes(api: Api, routes):
    for route in routes:
        api.add_resource(route[0], route[1])
