from testUtils import requestExpect
class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.get("/backend/game/1/page/", 200, [], {
            "game_id": "1",
            "gamePage": "test"
        })

    def __del__(self):
        pass
