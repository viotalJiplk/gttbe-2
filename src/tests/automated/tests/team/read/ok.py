from testUtils import getJws, requestExpect
from copy import deepcopy

result = {
    "name": "India",
    "teamId": 1,
    "gameId": 6,
    "Players": [
        {
            "userid": "914450748079974600",
            "nick": "AJwpGdDq",
            "role": "Captain"
        }, {
            "userid": "183190492953263839",
            "nick": "NXHQvsww",
            "role": "Member"
        }, {
            "userid": "765775025559645184",
            "nick": "JtnDmQKK",
            "role": "Member"
        }, {
            "userid": "609174111951229484",
            "nick": "tKncBSwU",
            "role": "Reservist"
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
