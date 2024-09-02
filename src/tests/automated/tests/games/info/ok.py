from testUtils import requestExpect
class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.get("/backend/game/1/", 200, [], {
            "gameId": 1,
            "name": "COUNTER_STRIKE",
            "registrationStart": "2024-01-29",
            "registrationEnd": "2025-02-21",
            "maxTeams": 16
        })

    def __del__(self):
        pass
