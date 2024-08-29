from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "stageId":1,
    "firstTeamId":1,
    "secondTeamId":2,
    "firstTeamResult":16,
    "secondTeamResult":0
}
read = deepcopy(create)
read["matchId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/match/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )
        matchId = res["matchId"]
        requestExpect.get(f"/backend/match/{matchId}/", 200, {},  read)

    def __del__(self):
        pass