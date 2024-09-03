from testUtils import getJws, requestExpect

create = {
    "permission": "assignedRole.read",
    "generatedRoleId": 1,
    "gameId": None,
    "eligible": False,
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/generatedRolePermission/create", create, 401)

    def __del__(self):
        pass
