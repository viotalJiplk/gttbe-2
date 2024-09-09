from .request import requestExpect

def getJws(userId):
    res = requestExpect.get(f"/backend/jwsfortestingonly/{userId}/", 200)
    res = res.split(" ")[1]
    return res
