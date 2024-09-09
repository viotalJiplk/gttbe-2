from functools import wraps
from flask_restful import request
from flask_restx import fields
from .date import dateFromString, timeFromString
from datetime import date, time
from .errorListFile import errorList
from utils import ReturnableError
from .error import handleReturnableError
import datetime
from .register import expectsJson
from shared.utils import genState
from typing import Callable

class Null(fields.Raw):
    __schema_type__ = ['null']
    __schema_example__ = None

class NullableInt(fields.Integer):
    __schema_type__ = ['integer', 'null']
    __schema_example__ = 0

class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 0

def toSwaggerDict(expectedJson: dict = {}, required: bool = True):
    swaggerDict = {}
    for key, value in expectedJson.items():
        if len(value) == 1:
            if value[0] is int:
                swaggerDict[key] = fields.Integer(required=required)
            elif value[0] is str:
                swaggerDict[key] = fields.String(required=required)
            elif value[0] is bool:
                swaggerDict[key] = fields.Boolean(required=required)
            elif value[0] is type(None):
                swaggerDict[key] = Null(required=required)
            elif value[0] is datetime.date:
                swaggerDict[key] = fields.Date(required=required)
            elif value[0] is datetime.time:
                swaggerDict[key] = fields.String(required=required, pattern=r"((0?\d)|(1[0-2])):[0-5]?\d:[0-5]?\d")
            else:
                raise Exception(f"Unknown type {value[0]}")
        elif len(value) == 2:
            if int in value and type(None) in value:
                swaggerDict[key] = NullableInt
            elif str in value and type(None) in value:
                swaggerDict[key] = NullableString
            else:
                raise Exception(f"Unknown type {value[0]}, {value[1]}")
        else:
            raise Exception(f"Unknown type {value}")
    return swaggerDict

def postJson(jsonParams:dict={}):
    """Decorator that Gets json from request
    call: func(data=data, *args, **kwargs)

    Args:
        jsonParams (dict, optional): expected json. Defaults to {} continues on missing.
    """

    swaggerDict = toSwaggerDict(jsonParams, False)
    def wrapper(func: Callable):
        @expectsJson(f"{str(func.__module__)}.{str(func.__name__)}", swaggerDict)
        @wraps(func)
        @handleReturnableError
        def wrapPostJson(*args, **kwargs):
            try:
                data = request.get_json()
            except:
                raise errorList.json.notValidJson
            return func(data=data, *args, **kwargs)
        return wrapPostJson
    return wrapper

def postJsonParse(expectedJson:dict={}):
    """Decorator that gets and validates json from request
    call: func(data=data, *args, **kwargs)

    Args:
        expectedJson (dict, optional): expected json. Defaults to {} throws on missing.
    """
    swaggerDict = toSwaggerDict(expectedJson, True)

    def wrapper(func: Callable):
        @expectsJson(f"{str(func.__module__)}.{str(func.__name__)}", swaggerDict)
        @wraps(func)
        @handleReturnableError
        def wrapPostJson(*args, **kwargs):
            try:
                data = request.get_json()
            except:
                raise errorList.json.notValidJson
            for key, value in expectedJson.items():
                if key not in data:
                    raise ReturnableError(f"Missing key '{key}' in request.", "JSON", 401)
                if type(data[key]) == str and date in value:
                    data[key] = dateFromString(data[key])
                elif type(data[key]) == str and time in value:
                    data[key] = timeFromString(data[key])
                elif type(data[key]) == str and int in value:
                    try:
                        data[key] = int(data[key])
                    except ValueError:
                        raise ReturnableError(f"Value of key '{key}' does not have expected type '{str(value)}' type '{str(type(data[key]))}' found instead.", "JSON", 401)
                elif type(data[key]) not in value:
                    raise ReturnableError(f"Value of key '{key}' does not have expected type '{str(value)}' type '{str(type(data[key]))}' found instead.", "JSON", 401)
            return func(data=data, *args, **kwargs)
        return wrapPostJson
    return wrapper

def setAttributeFromList(obj: object, data: dict, accessibleAttributes: dict):
    """Sets attributes from dict on object (data["test"]) -> obj.test

    Args:
        obj (object): object to set attributes on
        data (dict): dict to set attributes from
        accessibleAttributes (dict): list accessible attributes on object

    Raises:
        errorList.data.couldNotConvertInt: unable to convert int from str
        errorList.data.unableToConvert: unable to convert type
    """
    for x in data:
        if x in accessibleAttributes:
            if type(data[x]) in accessibleAttributes[x]:
                setattr(obj, x, data[x])
            elif type(data[x]) == str and date in accessibleAttributes[x]:
                setattr(obj, x, dateFromString(data[x]))
            elif type(data[x]) == str and time in accessibleAttributes[x]:
                setattr(obj, x, timeFromString(data[x]))
            elif type(data[x]) == str and int in accessibleAttributes[x]:
                try:
                    setattr(obj, x, int(data[x]))
                except ValueError:
                    raise errorList.data.couldNotConvertInt
            else:
                raise errorList.data.unableToConvert
