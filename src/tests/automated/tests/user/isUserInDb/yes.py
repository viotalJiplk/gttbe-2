from testUtils import getJws, requestExpect
from copy import deepcopy

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/user/114316488057882015/exists", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, {"exists": True}
        )

    def __del__(self):
        pass
