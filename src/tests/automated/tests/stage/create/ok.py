from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "eventId":1,
    "stageName":"XD",
    "stageIndex":0
}
result = deepcopy(create)
result["stageId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/stage/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
