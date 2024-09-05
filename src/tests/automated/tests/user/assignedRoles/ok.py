from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
        {
            "assignedRoleId": 1,
            "roleName": "admin",
            "discordRoleId": None
        },
        {
            "assignedRoleId": 3,
            "roleName": "user",
            "discordRoleId": None
        },
        {
            "assignedRoleId": 4,
            "roleName": "public",
            "discordRoleId": None
        }
    ]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/user/@me/assignedRoles/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
