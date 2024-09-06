from testUtils import getJws, requestExpect
from copy import deepcopy

result = [
    {
        "stageId": 1,
        "eventId": 1,
        "stageName": "LOL quarterfinals",
        "stageIndex": 1
    },
    {
        "stageId": 2,
        "eventId": 1,
        "stageName": "LOL semifinals",
        "stageIndex": 2
    },
    {
        "stageId": 3,
        "eventId": 1,
        "stageName": "LOL finals",
        "stageIndex": 3
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/event/1/stages/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
