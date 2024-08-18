from testUtils import requestExpect

result = [
  {
    "teamId": 8,
    "name": "Golf",
    "nick": "stEhdFTw",
    "role": "Reservist",
    "canPlaySince": "2024-05-26T16:20:45"
  },
  {
    "teamId": 8,
    "name": "Golf",
    "nick": "SyStwgjT",
    "role": "Member",
    "canPlaySince": "2024-05-26T16:20:45"
  },
  {
    "teamId": 8,
    "name": "Golf",
    "nick": "goGUVwaz",
    "role": "Member",
    "canPlaySince": "2024-05-26T16:20:45"
  },
  {
    "teamId": 8,
    "name": "Golf",
    "nick": "awWrQlgD",
    "role": "Member",
    "canPlaySince": "2024-05-26T16:20:45"
  },
  {
    "teamId": 8,
    "name": "Golf",
    "nick": "cqoMPoRb",
    "role": "Captain",
    "canPlaySince": "2024-05-26T16:20:45"
  },
  {
    "teamId": 8,
    "name": "Golf",
    "nick": "AWFjRMHg",
    "role": "Member",
    "canPlaySince": "2024-05-26T16:20:45"
  }
]


class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.get("/backend/team/list/participating/5/false", 200, {}), result

    def __del__(self):
        pass
