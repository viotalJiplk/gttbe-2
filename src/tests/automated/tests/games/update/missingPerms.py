from testUtils import requestExpect

update = {
    "gameId": 1,
    "name": "COUNTER_STRIKE",
    "registrationStart": "2024-01-29",
    "registrationEnd": "2024-01-29",
    "maxCaptains": 1,
    "maxMembers": 2,
    "maxReservists": 3,
    "minCaptains": 1,
    "minMembers": 1,
    "minReservists": 0,
    "maxTeams": 0
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.put("/backend/game/1/", update, 401)

    def __del__(self):
        pass
