from flask_restx import Namespace, Resource, fields
from typing import List, Tuple
from .objectTesterFile import objectTester

class ExpectParams:
    def __init__(self, name, expect, validate, strict):
        self.name = name
        self.expect = expect
        self.validate = validate
        self.strict = strict

class ReturnParams:
    def __init__(self, name, returns, code, asList, strict, description):
        self.name = name
        self.returns = returns
        self.code = code
        self.asList = asList
        self.strict = strict
        self.description = description

def expectsJson(name, expect, validate=False, strict=False):
    def wrapper(func):
        func.__expect = ExpectParams(name, expect, validate, strict)
        return func
    return wrapper

def returnsJson(name, returns, code=200, asList=False, strict=False, description=''):
    def wrapper(func):
        func.__returns = ReturnParams(name, returns, code, asList, strict, description)
        return func
    return wrapper

def registerRoutes(api: Namespace, routes: list[Tuple[Resource, str]]):
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
    def __return(method):
        if hasattr(method, "__returns") and isinstance(method.__returns, ReturnParams):
            model = None
            if isinstance(method.__returns.returns, dict):
                model = api.model(name=method.__returns.name, model=method.__returns.returns, strict=method.__returns.strict)
            else:
                model = method.__returns.returns
            if method.__returns.asList:
                method = api.response(code=method.__returns.code, description=method.__returns.description,  model=[model])(method)
            else:
                method = api.response(code=method.__returns.code, description=method.__returns.description,  model=model)(method)
        return method

    for route in routes:
        if  hasattr(route[0], "get"):
            route[0].get = __expect(route[0].get)
            route[0].get = __return(route[0].get)
        if  hasattr(route[0], "head"):
            route[0].head = __expect(route[0].head)
            route[0].head = __return(route[0].head)
        if  hasattr(route[0], "post"):
            route[0].post = __expect(route[0].post)
            route[0].post = __return(route[0].post)
        if  hasattr(route[0], "put"):
            route[0].put = __expect(route[0].put)
            route[0].put = __return(route[0].put)
        if  hasattr(route[0], "delete"):
            route[0].delete = __expect(route[0].delete)
            route[0].delete = __return(route[0].delete)
        if  hasattr(route[0], "connect"):
            route[0].connect = __expect(route[0].connect)
            route[0].connect = __return(route[0].connect)
        if  hasattr(route[0], "options"):
            route[0].options = __expect(route[0].options)
            route[0].options = __return(route[0].options)
        if  hasattr(route[0], "trace"):
            route[0].trace = __expect(route[0].trace)
            route[0].trace = __return(route[0].trace)
        if  hasattr(route[0], "patch"):
            route[0].patch = __expect(route[0].patch)
            route[0].patch = __return(route[0].patch)
        api.add_resource(route[0], route[1])
