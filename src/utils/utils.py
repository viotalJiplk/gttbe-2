from functools import wraps
from flask_restful import request

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