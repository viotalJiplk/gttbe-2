from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "eventId":1,
    "stageName":"XD",
    "stageIndex":0
}
read = deepcopy(create)
read["stageId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/stage/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )
        stageId = res["stageId"]
        requestExpect.delete(f"/backend/stage/{stageId}/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )
        res = requestExpect.get(f"/backend/stage/{stageId}/", 404, {}
        )

    def __del__(self):
        pass
