from functools import wraps
from flask_restful import request

def postJson(func):
    @wraps(func)
    def wrapPostJson(*args, **kwargs):
        try:
            data = request.get_json()
        except:
            return {"kind": "JSON", "msg": "The date you sent is not a valid json."}, 401
        return func(data=data, *args, **kwargs)
    return wrapPostJson