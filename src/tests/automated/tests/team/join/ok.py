from testUtils import getJws, requestExpect
from copy import deepcopy
from datetime import datetime, timedelta

join = {
    "nick":"winner",
    "rank": 4,
    "max_rank": 6,
    "role": "Reservist"
}
result = {
    "name": "Alpha",
    "teamId": 7,
    "gameId": 4,
    "Players":[
        {
            "userid": "127705315212148643",
            "nick": "aSGCENNA",
            "role": "Captain"
        }, {
            "userid": "788530474257249249",
            "nick": "VCYfccLv",
            "role": "Member"
        }, {
            "userid": "520784028952126515",
            "nick": "CmgYaDjZ",
            "role": "Reservist"
        },{
            "userid": "800618827210965495",
            "nick": "EvNdqWrq",
            "role": "Reservist"
        },{
            "userid": "819559661680635792",
            "nick": "sBXYANzZ",
            "role": "Reservist"
        },{
            "userid": "114316488057882015",
            "nick": "winner",
            "role": "Reservist"
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
