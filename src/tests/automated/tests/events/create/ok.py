from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
        "date":"2023-07-08",
        "beginTime":"19:00:00",
        "endTime":"21:00:00",
        "gameId": 2,
        "description":"gg",
        "eventType":"PlayOff"
    }
result = deepcopy(create)
result["eventId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/event/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
