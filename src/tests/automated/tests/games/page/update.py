from testUtils import getJws, requestExpect

update = {"game_id": "1","gamePage":"test123"}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.put("/backend/game/1/page", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )
        requestExpect.get("/backend/game/1/page", 200, {},  update
        )

    def __del__(self):
        pass
