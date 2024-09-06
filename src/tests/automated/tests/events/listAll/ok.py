from testUtils import getJws, requestExpect
from copy import deepcopy

result = [
    {
        "eventId": 1,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    },
    {
        "eventId": 2,
        "date": "2023-11-17",
        "beginTime": "18:00",
        "endTime": "22:00",
        "gameId": 5,
        "description": "Valorant Playoff",
        "eventType": "playoff"
    },
    {
        "eventId": 3,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    },
    {
        "eventId": 5,
        "date": "2023-11-19",
        "beginTime": "13:00",
        "endTime": "18:00",
        "gameId": 3,
        "description": "Minecreaft Playoff",
        "eventType": "playoff"
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/event/listAll", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
