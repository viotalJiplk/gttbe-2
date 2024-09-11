from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "roleName": "testRole",
    "discordRoleId": None,
    "discordRoleIdEligible": None,
    "gameId": 1,
    "default": False,
    "minimal": 1,
    "maximal": 10
}

result = deepcopy(create)
result["generatedRoleId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/generatedRole/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        generatedRoleId = res["generatedRoleId"]
        result["generatedRoleId"] = generatedRoleId
        res = requestExpect.get(f"/backend/generatedRole/{generatedRoleId}/", 200, {}, result)

    def __del__(self):
        pass
