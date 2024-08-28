from testUtils import getJws, requestExpect
from copy import deepcopy

read = [
        "event.create",
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
        "user.readMe",
        "user.updateMe",
        "user.deleteMe",
        "user.exists",
        "user.permsListMe",
        "user.listTeamsMe",
        "team.create",
        "team.join",
        "team.genJoinStrMy",
        "team.leave",
        "team.kickTeam",
        "event.read",
        "game.listAll",
        "gamePage.read",
        "stage.read",
        "match.read",
        "page.read",
        "school.listAll",
        "team.listPartic",
        "team.read"
    ]

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get("/backend/user/@me/permissions/1", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
