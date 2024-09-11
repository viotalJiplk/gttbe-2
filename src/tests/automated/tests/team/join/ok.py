from testUtils import getJws, requestExpect
from copy import deepcopy
from datetime import datetime, timedelta

join = {
    "nick":"winner",
    "rank": 4,
    "max_rank": 6,
    "generatedRoleId": 8
}
result = {
    "name": "Alpha",
    "teamId": 7,
    "gameId": 4,
    "Players": [
        {
            "userId": "122891840080562664",
            "nick": "CmgYaDjZ",
            "generatedRoleId": 7
        },
        {
            "userId": "135346983583891046",
            "nick": "aSGCENNA",
            "generatedRoleId": 8
        },
        {
            "userId": "210568825432375324",
            "nick": "EvNdqWrq",
            "generatedRoleId": 8
        },
        {
            "userId": "774007414509236186",
            "nick": "sBXYANzZ",
            "generatedRoleId": 8
        },
        {
            "userId": "798209625306537808",
            "nick": "VCYfccLv",
            "generatedRoleId": 8
        },
        {
            "userId": "114316488057882015",
            "nick": "winner",
            "generatedRoleId": 8
        }
    ]
}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        requestExpect.put("/backend/game/4/", {
                "registrationEnd": tomorrow,
                "maxReservists": 10,
            }, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )
        requestExpect.post("/backend/team/id/7/join/qoMMHyH5Md", join, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )
        requestExpect.get("/backend/team/id/7/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
