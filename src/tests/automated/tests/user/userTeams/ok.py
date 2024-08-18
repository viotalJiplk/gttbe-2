from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
    {"teamId": 23, "nick": "dZGgAVQF", "role": "Member", "name": "Foxtrot", "gameId": 5}
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/user/279366087609404974/teams/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
