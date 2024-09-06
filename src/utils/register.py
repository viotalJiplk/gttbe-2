from flask_restx import Api, Resource
from typing import List, Tuple

def registerRoutes(api: Api, routes: list[Tuple[Resource, str]]):
    """Registers new endpoints

    Args:
        api (Api): api to register endpoints to
        routes (list[Tuple[Resource, str]]): endpoint to register
    """
    for route in routes:
        api.add_resource(route[0], route[1])
