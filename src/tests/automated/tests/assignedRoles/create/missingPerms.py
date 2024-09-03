from testUtils import getJws, requestExpect

create = {
    "roleName": "testRole",
    "discordRoleId": None,
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/assignedRole/create", create, 401)

    def __del__(self):
        pass
