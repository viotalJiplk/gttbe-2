from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
    {
        "generatedRoleId": 1,
        "roleName": "Kapitán",
        "discordRoleId": None,
        "discordRoleIdEligible": None,
        "gameId": 1,
        "default": 1,
        "minimal": 1,
        "maximal": 1
    },
    {
        "generatedRoleId": 2,
        "roleName": "Hráč",
        "discordRoleId": None,
        "discordRoleIdEligible": None,
        "gameId": 1,
        "default": 0,
        "minimal": 4,
        "maximal": 8
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/generatedRole/list/1/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
