from testUtils import getJws, requestExpect

create = {
    "stageId":1,
    "firstTeamId":1,
    "secondTeamId":2,
    "firstTeamResult":16,
    "secondTeamResult":0
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/match/create", create, 401)

    def __del__(self):
        pass
