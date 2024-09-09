from flask_restx import Api, Resource
from typing import List, Tuple

class ExpectParams:
    def __init__(self, name, expect, validate, strict):
        self.name = name
        self.expect = expect
        self.validate = validate
        self.strict = strict

def expectsJson(name, expect, validate=False, strict=False):
    def wrapper(func):
        func.__expect = ExpectParams(name, expect, validate, strict)
        return func
    return wrapper

def registerRoutes(api: Api, routes: list[Tuple[Resource, str]]):
    """Registers new endpoints

    Args:
        api (Api): api to register endpoints to
        routes (list[Tuple[Resource, str]]): endpoint to register
    """
    def __expect(method):
        if hasattr(method, "__expect") and isinstance(method.__expect, ExpectParams):
            model = api.model(name=method.__expect.name, model=method.__expect.expect, strict=method.__expect.strict)
            method = api.expect(model, validate=method.__expect.validate)(method)
        return method
    for route in routes:
        if  hasattr(route[0], "get"):
            route[0].get = __expect(route[0].get)
        if  hasattr(route[0], "head"):
            route[0].head = __expect(route[0].head)
        if  hasattr(route[0], "post"):
            route[0].post = __expect(route[0].post)
        if  hasattr(route[0], "put"):
            route[0].put = __expect(route[0].put)
        if  hasattr(route[0], "delete"):
            route[0].delete = __expect(route[0].delete)
        if  hasattr(route[0], "connect"):
            route[0].connect = __expect(route[0].connect)
        if  hasattr(route[0], "options"):
            route[0].options = __expect(route[0].options)
        if  hasattr(route[0], "trace"):
            route[0].trace = __expect(route[0].trace)
        if  hasattr(route[0], "patch"):
            route[0].patch = __expect(route[0].patch)
        api.add_resource(route[0], route[1])
