from testUtils import getJws, requestExpect
from copy import deepcopy

read = {
    "userId": 114316488057882015,
    "surname": "Jones",
    "name": "David",
    "adult": 1,
    "schoolId": 663,
    "discord_user_object": None
    }

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/user/114316488057882015/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
