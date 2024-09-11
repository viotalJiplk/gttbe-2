from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
        "date":"2023-07-08",
        "beginTime":"19:00:00",
        "endTime":"21:00:00",
        "gameId":2,
        "description":"gg",
        "eventType":"PlayOff"
    }
read = deepcopy(create)
read["eventId"] = int

update = {
        "date":"2024-07-08",
        "beginTime":"22:00:00",
        "endTime":"23:00:00",
        "gameId":3,
        "description":"gg2021",
        "eventType":"PlayOff"
    }
updateRead = deepcopy(update)
updateRead["eventId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/event/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )
        eventId = res["eventId"]
        requestExpect.put(f"/backend/event/{eventId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/event/{eventId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
