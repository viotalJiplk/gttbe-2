from testUtils import getJws, requestExpect

create = {
    "eventId":1,
    "stageName":"XD",
    "stageIndex":0
}

class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.post("/backend/stage/create", create, 401)

    def __del__(self):
        pass
