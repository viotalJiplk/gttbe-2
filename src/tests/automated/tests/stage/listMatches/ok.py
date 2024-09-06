from testUtils import getJws, requestExpect
from copy import deepcopy

result = [
    {
        "matchId": 1,
        "stageId": 1,
        "firstTeamId": 0,
        "secondTeamId": 10,
        "firstTeamResult": 12,
        "secondTeamResult": 1,
        "eventId": 1,
        "stageName": "LOL quarterfinals",
        "stageIndex": 1,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    },
    {
        "matchId": 2,
        "stageId": 1,
        "firstTeamId": 12,
        "secondTeamId": 18,
        "firstTeamResult": 5,
        "secondTeamResult": 0,
        "eventId": 1,
        "stageName": "LOL quarterfinals",
        "stageIndex": 1,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    },
    {
        "matchId": 3,
        "stageId": 1,
        "firstTeamId": 20,
        "secondTeamId": 28,
        "firstTeamResult": 6,
        "secondTeamResult": 9,
        "eventId": 1,
        "stageName": "LOL quarterfinals",
        "stageIndex": 1,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    },
    {
        "matchId": 4,
        "stageId": 1,
        "firstTeamId": 29,
        "secondTeamId": 47,
        "firstTeamResult": 10,
        "secondTeamResult": 5,
        "eventId": 1,
        "stageName": "LOL quarterfinals",
        "stageIndex": 1,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    },
    {
        "matchId": 6,
        "stageId": 1,
        "firstTeamId": 1,
        "secondTeamId": 2,
        "firstTeamResult": 16,
        "secondTeamResult": 2,
        "eventId": 1,
        "stageName": "LOL quarterfinals",
        "stageIndex": 1,
        "date": "2023-07-07",
        "beginTime": "18:00",
        "endTime": "20:00",
        "gameId": 1,
        "description": "",
        "eventType": "PlayOff"
    }
]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/stage/1/matches/", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )

    def __del__(self):
        pass
