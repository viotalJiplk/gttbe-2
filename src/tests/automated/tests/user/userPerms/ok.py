from testUtils import getJws, requestExpect
from copy import deepcopy
from json import dump

read = [
        {
            "permission": "team.create",
            "gameId": None
        },
        {
            "permission": "team.generateJoinStringMy",
            "gameId": None
        },
        {
            "permission": "team.join",
            "gameId": None
        },
        {
            "permission": "team.kickTeam",
            "gameId": None
        },
        {
            "permission": "team.leave",
            "gameId": None
        },
        {
            "permission": "user.deleteMe",
            "gameId": None
        },
        {
            "permission": "user.exists",
            "gameId": None
        },
        {
            "permission": "user.listTeamsMe",
            "gameId": None
        },
        {
            "permission": "user.permsListMe",
            "gameId": None
        },
        {
            "permission": "user.readMe",
            "gameId": None
        },
        {
            "permission": "user.updateMe",
            "gameId": None
        },
        {
            "permission": "event.listAll",
            "gameId": None
        },
        {
            "permission": "event.read",
            "gameId": None
        },
        {
            "permission": "game.listAll",
            "gameId": None
        },
        {
            "permission": "gamePage.read",
            "gameId": None
        },
        {
            "permission": "match.read",
            "gameId": None
        },
        {
            "permission": "page.read",
            "gameId": None
        },
        {
            "permission": "school.listAll",
            "gameId": None
        },
        {
            "permission": "stage.read",
            "gameId": None
        },
        {
            "permission": "team.listParticipating",
            "gameId": None
        },
        {
            "permission": "team.read",
            "gameId": None
        },
        {
            "permission": "assignedRole.read",
            "gameId": None
        },
        {
            "permission": "assignedRolePermission.read",
            "gameId": None
        },
        {
            "permission": "generatedRole.read",
            "gameId": None
        },
        {
            "permission": "generatedRolePermission.read",
            "gameId": None
        },
        {
            "permission": "userRole.read",
            "gameId": None
        },
        {
            "permission": "user.generatedRolesListMe",
            "gameId": None
        },
        {
            "permission": "user.assignedRolesList",
            "gameId": None
        }
    ]

class Test:
    def __init__(self):
        self.jws = getJws("	115423241599600111")

    def run(self):
        res = requestExpect.get("/backend/user/@me/permissions/1", 200,
            {
                "Authorization":f"Bearer {self.jws}",
            }, read
        )

    def __del__(self):
        pass
