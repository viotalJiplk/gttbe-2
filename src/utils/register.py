from flask_restx import Namespace, Resource, fields
from typing import List, Tuple
from .objectTesterFile import objectTester
import datetime

class ExpectParams:
    def __init__(self, name, expect, validate, strict, required):
        self.name = name
        self.expect = expect
        self.validate = validate
        self.strict = strict
        self.required = required

class ReturnParams:
    def __init__(self, name, returns, code, asList, strict, description, required):
        self.name = name
        self.returns = returns
        self.code = code
        self.asList = asList
        self.strict = strict
        self.description = description
        self.required = required

class Null(fields.Raw):
    __schema_type__ = ['null']
    __schema_example__ = None

class NullableInt(fields.Integer):
    __schema_type__ = ['integer', 'null']
    __schema_example__ = 0

class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 0

def toSwaggerDict(api: Namespace, prefix: str, expectedJson: dict|list = {}, required: bool = True, strict: bool = False):
    def __resolveKey(api, key, value):
        if isinstance(value, dict):
            nested = toSwaggerDict(api, prefix + key, value, required, strict)
            model = api.model(prefix + key, nested, None, strict)
            return fields.Nested(model)
        elif len(value) == 1:
            if value[0] is int:
                return fields.Integer(required=required)
            elif value[0] is str:
                return fields.String(required=required)
            elif value[0] is bool:
                return fields.Boolean(required=required)
            elif value[0] is type(None):
                return Null(required=required)
            elif value[0] is datetime.date:
                return fields.Date(required=required)
            elif value[0] is datetime.time:
                return fields.String(required=required, pattern=r"((0?\d)|(1[0-2])):[0-5]?\d:[0-5]?\d")
            else:
                raise Exception(f"Unknown type {value[0]}")
        elif len(value) == 2:
            if int in value and type(None) in value:
                return NullableInt
            elif str in value and type(None) in value:
                return NullableString
            else:
                raise Exception(f"Unknown type {value[0]}, {value[1]}")
        else:
            raise Exception(f"Unknown type {value}")
    if isinstance(expectedJson, dict):
        swaggerDict = {}
        for key, value in expectedJson.items():
            swaggerDict[key] = __resolveKey(api, key, value)
        return swaggerDict
    elif isinstance(expectedJson, list):
        return __resolveKey(api, '', expectedJson)
    else:
        raise ValueError("Unsupported type!")

def expectsJson(name, expect, validate=False, strict=False, required = False):
    def wrapper(func):
        func.__expect = ExpectParams(name, expect, validate, strict, required)
        return func
    return wrapper

def returnsJson(name, returns, code=200, asList=False, strict=False, description='', required = False):
    def wrapper(func):
        if not hasattr(func, "__returns"):
            func.__returns = []
        func.__returns.append(ReturnParams(name, returns, code, asList, strict, description, required))
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
            model = api.model(name=method.__expect.name, model=toSwaggerDict(api, method.__expect.name, method.__expect.expect, method.__expect.required, method.__expect.strict), strict=method.__expect.strict)
            method = api.expect(model, validate=method.__expect.validate)(method)
        return method
    def __return(method):
        methodCopy = method
        if hasattr(method, "__returns"):
            for ret in method.__returns:
                if isinstance(ret, ReturnParams):
                    model = None
                    if isinstance(ret.returns, dict):
                        model = api.model(name=ret.name, model=toSwaggerDict(api, ret.name, ret.returns, ret.required, ret.strict), strict=ret.strict)
                    else:
                        model = ret.returns
                    if ret.asList:
                        methodCopy = api.response(code=ret.code, description=ret.description,  model=[model])(methodCopy)
                    else:
                        methodCopy = api.response(code=ret.code, description=ret.description,  model=model)(methodCopy)
        return methodCopy

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
