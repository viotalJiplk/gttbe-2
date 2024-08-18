from testUtils import getJws, requestExpect
from copy import deepcopy

read = ["event.create",
        "event.update",
        "event.delete",
        "gamePage.update",
        "game.update",
        "stage.create",
        "stage.update",
        "stage.delete",
        "match.create",
        "match.update",
        "match.delete",
        "user.read",
        "user.update",
        "user.delete",
        "user.permissionList",
        "user.listTeams",
        "team.listParticDisc",
        "team.genJoinStr",
        "team.kick",
        "event.listAll",
        "event.read",
        "game.listAll",
        "gamePage.read",
        "match.read",
        "page.read",
        "school.listAll",
        "stage.read",
        "team.create",
        "team.genJoinStrMy",
        "team.join",
        "team.kickTeam",
        "team.leave",
        "team.listPartic",
        "team.read",
        "user.deleteMe",
        "user.exists",
        "user.listTeamsMe",
        "user.permsListMe",
        "user.readMe",
        "user.updateMe"
    ]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.get("/backend/user/@me/permissions/1", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
