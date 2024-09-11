from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "eventId":1,
    "stageName":"XD",
    "stageIndex":0
}
read = deepcopy(create)
read["stageId"] = int

update = {
    "eventId":2,
    "stageName":"XD2",
    "stageIndex":4
}
updateRead = deepcopy(update)
updateRead["stageId"] = int

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
        requestExpect.put(f"/backend/stage/{stageId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/stage/{stageId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
