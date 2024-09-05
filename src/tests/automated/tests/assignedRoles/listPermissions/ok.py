from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
  {
    "assignedRolePermissionId": int,
    "permission": "school.listAll",
    "gameId": 4,
    "assignedRoleId": 2
  }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get(f"/backend/assignedRole/2/permissions/", 200, {},  read)

    def __del__(self):
        pass
