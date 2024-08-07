from functools import wraps
from flask_restful import request
from utils.date import dateFromString, timeFromString
from datetime import date, time
from utils.errorList import errorList

def postJson(func):
    @wraps(func)
    def wrapPostJson(*args, **kwargs):
        try:
            data = request.get_json()
        except:
            return {"kind": "JSON", "msg": "The data you sent is not a valid json."}, 401
        return func(data=data, *args, **kwargs)
    return wrapPostJson

def postJsonParse(expectedJson:dict={}):
    def wrapper(func):
        @wraps(func)
        def wrapPostJson(*args, **kwargs):
            try:
                data = request.get_json()
            except:
                return {"kind": "JSON", "msg": "The data you sent is not a valid json."}, 401
            for key, value in expectedJson.items():
                if key not in data:
                    return {"kind": "JSON", "msg": f"Missing key '{key}' in request."}, 401
                if type(data[key])  not in value:
                    return {"kind": "JSON", "msg": f"Value of key '{key}' does not have expected type '{str(value)}' type '{str(type(data[key]))}' found instead."}, 401
            return func(data=data, *args, **kwargs)
        return wrapPostJson
    return wrapper

def setAttributeFromList(obj, data, accessibleAttributes):
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
