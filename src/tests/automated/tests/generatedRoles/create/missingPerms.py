from testUtils import getJws, requestExpect

create = {
    "roleName": "testRole",
    "discordRoleId": None,
    "discordRoleIdEligible": None,
    "gameId": 1,
    "default": False,
    "minimal": 1,
    "maximal": 10
}

class Test:
    def __init__(self):
        pass

    def run(self):
        res = requestExpect.post("/backend/generatedRole/create/", create, 401)

    def __del__(self):
        pass
