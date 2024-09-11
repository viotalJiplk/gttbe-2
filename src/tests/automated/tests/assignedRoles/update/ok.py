from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "roleName": "testRole",
    "discordRoleId": None,
}
result = deepcopy(create)
result["assignedRoleId"] = int

update = {
    "roleName": "testRole123",
    "discordRoleId": 1,
}
updateRead = deepcopy(update)
updateRead["assignedRoleId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/assignedRole/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        assignedRoleId = res["assignedRoleId"]
        updateRead["assignedRoleId"] = assignedRoleId
        requestExpect.put(f"/backend/assignedRole/{assignedRoleId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/assignedRole/{assignedRoleId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
