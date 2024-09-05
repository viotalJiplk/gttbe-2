from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
    {
        "generatedRolePermissionId": 1,
        "permission": "school.listAll",
        "generatedRoleId": 1,
        "gameId": 1,
        "eligible": 1
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get(f"/backend/generatedRole/1/permissions/", 200, {},  read)

    def __del__(self):
        pass
