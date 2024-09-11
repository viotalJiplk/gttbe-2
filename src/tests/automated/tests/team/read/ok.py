from testUtils import getJws, requestExpect
from copy import deepcopy

result = {
    "name": "India",
    "teamId": 1,
    "gameId": 6,
    "Players": [
        {
            "userId": "315241566832246282",
            "nick": "tKncBSwU",
            "generatedRoleId": 11
        },
        {
            "userId": "817942517970237079",
            "nick": "NXHQvsww",
            "generatedRoleId": 12
        },
        {
            "userId": "859505747524140731",
            "nick": "AJwpGdDq",
            "generatedRoleId": 12
        },
        {
            "userId": "944849240707485390",
            "nick": "JtnDmQKK",
            "generatedRoleId": 12
        }
    ]
}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get("/backend/team/id/1/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
