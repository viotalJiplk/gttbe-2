from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "roleName": "testRole",
    "discordRoleId": None,
}

result = deepcopy(create)
result["assignedRoleId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/assignedRole/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
