from .request import requestExpect
from json import loads

def getJws(userId):
    res = requestExpect.get(f"/backend/jwsfortestingonly/{userId}/", 200)
    res = loads(res)
    if "jws" not in res:
        raise Exception("Jws return issue.")
    return res["jws"]
