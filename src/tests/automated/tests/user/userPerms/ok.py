from testUtils import getJws, requestExpect
from copy import deepcopy
from json import dump

class Test:
    def __init__(self):
        self.jws = getJws("	115423241599600111")

    def run(self):
        res = requestExpect.get("/backend/user/@me/permissions/1", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )

    def __del__(self):
        pass
