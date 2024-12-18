from testUtils import getJws, requestExpect
from copy import deepcopy

class Test:
    def __init__(self):
        self.jws = getJws("993504523045320908")

    def run(self):
        res = requestExpect.delete("/backend/user/@me/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )

    def __del__(self):
        pass
