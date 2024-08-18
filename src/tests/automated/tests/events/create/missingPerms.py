from testUtils import getJws, requestExpect

create = {
        "date":"2023-7-8",
        "beginTime":"19:00:00",
        "endTime":"21:00:00",
        "gameId":2,
        "description":"gg",
        "eventType":"PlayOff"
    }

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/event/create", create, 401)

    def __del__(self):
        pass
