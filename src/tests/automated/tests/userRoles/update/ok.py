from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "assignedRoleId": 1,
    "userId": "294425712404712387",
}

result = deepcopy(create)
result["userRoleId"] = int

update = {
    "assignedRoleId": 2,
    "userId": "303496896338022773",
}
updateRead = deepcopy(update)
updateRead["userRoleId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/userRole/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        userRoleId = res["userRoleId"]
        updateRead["userRoleId"] = userRoleId
        requestExpect.put(f"/backend/userRole/{userRoleId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/userRole/{userRoleId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
