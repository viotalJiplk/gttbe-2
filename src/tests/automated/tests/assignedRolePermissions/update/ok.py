from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "permission": "assignedRole.read",
    "gameId": None,
    "assignedRoleId": 1
}

result = deepcopy(create)
result["assignedRolePermissionId"] = int

update = {
    "permission": "assignedRole.update",
    "gameId": 4,
    "assignedRoleId": 2
}
updateRead = deepcopy(update)
updateRead["assignedRolePermissionId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/assignedRolePermission/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        assignedRolePermissionId = res["assignedRolePermissionId"]
        requestExpect.put(f"/backend/assignedRolePermission/{assignedRolePermissionId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/assignedRolePermission/{assignedRolePermissionId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
