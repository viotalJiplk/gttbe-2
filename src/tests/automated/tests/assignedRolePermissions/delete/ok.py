from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "permission": "assignedRole.read",
    "gameId": None,
    "assignedRoleId": 1
}

result = deepcopy(create)
result["assignedRolePermissionId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/assignedRolePermission/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        assignedRolePermissionId = res["assignedRolePermissionId"]
        requestExpect.delete(f"/backend/assignedRolePermission/{assignedRolePermissionId}/", 200, {
                "Authorization":f"Bearer {self.jws}",
        })
        res = requestExpect.get(f"/backend/assignedRolePermission/{assignedRolePermissionId}/", 404, {}
        )

    def __del__(self):
        pass