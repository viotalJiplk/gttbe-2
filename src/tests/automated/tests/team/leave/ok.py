from testUtils import getJws, requestExpect

result = {
    "name": "India",
    "teamId": 1,
    "gameId": 6,
    "Players": [
        {
            "userid": "914450748079974600",
            "nick": "AJwpGdDq",
            "role": "Captain"
        }, {
            "userid": "183190492953263839",
            "nick": "NXHQvsww",
            "role": "Member"
        }, {
            "userid": "765775025559645184",
            "nick": "JtnDmQKK",
            "role": "Member"
        }, {
            "userid": "609174111951229484",
            "nick": "tKncBSwU",
            "role": "Reservist"
        }
    ]
}
after = {
    "name": "India",
    "teamId": 1,
    "gameId": 6,
    "Players": [
        {
            "userid": "914450748079974600",
            "nick": "AJwpGdDq",
            "role": "Captain"
        }, {
            "userid": "183190492953263839",
            "nick": "NXHQvsww",
            "role": "Member"
        }, {
            "userid": "765775025559645184",
            "nick": "JtnDmQKK",
            "role": "Member"
        }
    ]
}

class Test:
    def __init__(self):
        self.jwsPriv = getJws("114316488057882015")
        self.jws = getJws("609174111951229484")

    def run(self):
        requestExpect.get("/backend/team/id/1/", 200,
            {
                "Authorization":f"Bearer {self.jwsPriv}",
            }, result
        )

        requestExpect.delete("/backend/team/id/1/kick/@me/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }
        )

        requestExpect.get("/backend/team/id/1/", 200,
            {
                "Authorization":f"Bearer {self.jwsPriv}",
            }, after
        )

    def __del__(self):
        pass
