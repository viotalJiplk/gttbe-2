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

update = {
    "roleName": "testRole123",
    "discordRoleId": "123",
    "discordRoleIdEligible": "456",
    "gameId": 2,
    "default": False,
    "minimal": 50,
    "maximal": 60
}
updateRead = deepcopy(update)
updateRead["generatedRoleId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/generatedRole/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        generatedRoleId = res["generatedRoleId"]
        updateRead["generatedRoleId"] = generatedRoleId
        requestExpect.put(f"/backend/generatedRole/{generatedRoleId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/generatedRole/{generatedRoleId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
