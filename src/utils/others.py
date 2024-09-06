from functools import wraps
from flask_restful import request
from .date import dateFromString, timeFromString
from datetime import date, time
from .errorListFile import errorList
from utils import ReturnableError
from .error import handleReturnableError

def postJson(func):
    """Decorator that Gets json from request
    call: func(data=data, *args, **kwargs)"""
    @wraps(func)
    @handleReturnableError
    def wrapPostJson(*args, **kwargs):
        try:
            data = request.get_json()
        except:
            raise errorList.json.notValidJson
        return func(data=data, *args, **kwargs)
    return wrapPostJson

def postJsonParse(expectedJson:dict={}):
    """Decorator that gets and validates json from request
    call: func(data=data, *args, **kwargs)

    Args:
        expectedJson (dict, optional): expected json. Defaults to {}.
    """
    def wrapper(func):
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
