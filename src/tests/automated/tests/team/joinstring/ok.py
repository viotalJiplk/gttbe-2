from testUtils import getJws, requestExpect
from copy import deepcopy
from datetime import datetime, timedelta

response = {
    "joinString": str
    }

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get("/backend/team/id/1/joinString", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, response
        )

    def __del__(self):
        pass
