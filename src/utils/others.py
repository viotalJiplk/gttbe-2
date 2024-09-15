from functools import wraps
from flask_restful import request
from flask_restx import fields
from .date import dateFromString, timeFromString
from .errorListFile import errorList
from utils import ReturnableError
from .error import handleReturnableError
from datetime import date, time
from .register import expectsJson, returnsJson
from typing import Callable

def formatUnique(func, suffix):
    return f"{str(func.__module__)}.{str(func.__qualname__)}.{suffix}".replace("<", "").replace(">", "").replace(" ", "_").replace(",", "")

def returnParser(returnJson: dict = {}, code: int = 200, asList: bool = False, strict: bool = False):
    def wrapper(func: Callable):
        returnsJson(formatUnique(func, "return"), returnJson, code, asList, strict, '', False)(func)
        return func
    return wrapper

def returnError(errors: list[ReturnableError]):
    def wrapper(func: Callable):
        for error in errors:
            returnsJson(formatUnique(func, "returnError"), error.returnModel(), error.httpStatusCode, False, False, 'Error', False)(func)
        return func
    return wrapper

def postJson(jsonParams:dict={}):
    """Decorator that Gets json from request
    call: func(data=data, *args, **kwargs)

    Args:
        jsonParams (dict, optional): expected json. Defaults to {} continues on missing.
    """

    def wrapper(func: Callable):
        @expectsJson(f"{str(func.__module__)}.{str(func.__qualname__)}.input", jsonParams, False, False, False)
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

    def wrapper(func: Callable):
        @expectsJson(f"{str(func.__module__)}.{str(func.__name__)}", expectedJson, False, False, True)
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
