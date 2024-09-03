from testUtils import getJws, requestExpect

create = {
    "permission": "assignedRole.read",
    "gameId": None,
    "assignedRoleId": 1
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/assignedRolePermission/create", create, 401)

    def __del__(self):
        pass
