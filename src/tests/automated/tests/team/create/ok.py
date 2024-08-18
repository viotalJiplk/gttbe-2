from testUtils import getJws, requestExpect
from copy import deepcopy
from datetime import datetime, timedelta

create = {
    "name":"testTeam",
    "game_id": 2,
    "nick":"winner",
    "rank": 4,
    "max_rank": 6
}
result = {
    "teamId": int,
    "gameId": 2,
    "name": "testTeam",
    "joinString": None
}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        requestExpect.put("/backend/game/2/", {
                "registrationEnd": tomorrow,
            }, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )
        res = requestExpect.post("/backend/team/create", create, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
