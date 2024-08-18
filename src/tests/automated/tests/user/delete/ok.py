from testUtils import getJws, requestExpect
from copy import deepcopy

class Test:
    def __init__(self):
        self.jws = getJws("800368402471736591")

    def run(self):
        res = requestExpect.delete("/backend/user/@me/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )

    def __del__(self):
        pass
