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

update = {
    "stageId":2,
    "firstTeamId":3,
    "secondTeamId":4,
    "firstTeamResult":0,
    "secondTeamResult":16
}
updateRead = deepcopy(update)
updateRead["matchId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/match/create/", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )
        matchId = res["matchId"]
        requestExpect.put(f"/backend/match/{matchId}/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, updateRead
        )
        res = requestExpect.get(f"/backend/match/{matchId}/", 200, {}, updateRead
        )

    def __del__(self):
        pass
