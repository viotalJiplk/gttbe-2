from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
    {
        "teamId": 23,
        "generatedRoleId": 9,
        "roleName": "Kapitán",
        "discordRoleId": None,
        "discordRoleIdEligible": None,
        "gameId": 5,
        "default": 1,
        "minimal": 1,
        "maximal": 1
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/user/@me/generatedRoles/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
