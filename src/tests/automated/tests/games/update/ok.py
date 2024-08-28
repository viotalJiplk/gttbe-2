from testUtils import getJws, requestExpect

update = {
    "gameId": 1,
    "name": "COUNTER_STRIKE1",
    "registrationStart": "2024-02-29",
    "registrationEnd": "2030-01-29",
    "maxTeams": 9
}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.put("/backend/game/1/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )
        requestExpect.get("/backend/game/1/", 200, {},  update)

    def __del__(self):
        pass
