from testUtils import getJws, requestExpect
from copy import deepcopy

update = {
    "name": "Name",
    "surname": "Surname",
    "adult": True,
    "schoolId": 2
}
read = {
    "userId": 114316488057882015,
    "surname": "Surname",
    "name": "Name",
    "adult": 1,
    "schoolId": 2,
    "discord_user_object": None
}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.put("/backend/user/114316488057882015/", update, 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )
        requestExpect.get("/backend/user/114316488057882015/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
