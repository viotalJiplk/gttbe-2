from testUtils import getJws, requestExpect

create = {
    "assignedRoleId": 1,
    "userId": "294425712404712387",
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/userRole/create", create, 401)

    def __del__(self):
        pass
