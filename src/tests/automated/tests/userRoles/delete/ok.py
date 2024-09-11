from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "assignedRoleId": 1,
    "userId": "294425712404712387",
}
result = deepcopy(create)
result["userRoleId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/userRole/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        userRoleId = res["userRoleId"]
        requestExpect.delete(f"/backend/userRole/{userRoleId}/", 200, {
                "Authorization":f"Bearer {self.jws}",
        })
        res = requestExpect.get(f"/backend/userRole/{userRoleId}/", 404, {}
        )

    def __del__(self):
        pass
