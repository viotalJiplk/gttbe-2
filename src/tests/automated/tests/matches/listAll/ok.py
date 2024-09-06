from testUtils import getJws, requestExpect
from copy import deepcopy

result = [
    {
        "matchId": 1,
        "stageId": 1,
        "firstTeamId": 0,
        "secondTeamId": 10,
        "firstTeamResult": 12,
        "secondTeamResult": 1
    },
    {
        "matchId": 2,
        "stageId": 1,
        "firstTeamId": 12,
        "secondTeamId": 18,
        "firstTeamResult": 5,
        "secondTeamResult": 0
    },
    {
        "matchId": 3,
        "stageId": 1,
        "firstTeamId": 20,
        "secondTeamId": 28,
        "firstTeamResult": 6,
        "secondTeamResult": 9
    },
    {
        "matchId": 4,
        "stageId": 1,
        "firstTeamId": 29,
        "secondTeamId": 47,
        "firstTeamResult": 10,
        "secondTeamResult": 5
    },
    {
        "matchId": 6,
        "stageId": 1,
        "firstTeamId": 1,
        "secondTeamId": 2,
        "firstTeamResult": 16,
        "secondTeamResult": 2
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/match/listAll/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
