from flask_restful import Resource, request
from routes.team.create import createTeam
from routes.team.list import ListTeam, ListParticipatingTeam
from routes.team.id import Team, TeamJoinstring, Join, Kick

class TeamDescr(Resource):
    def get(self):
        return [
            {
                "name": "create",
                "url": "create/",
                "type": "protected",
                "method": "POST",
                "descr": "Creates a team."
            },
            {
                "name": "Team",
                "url":"id/<teamId>/",
                "type": "public",
                "method": "GET",
                "descr": "Basic team info."
            },
            {
                "name": "generate_join_string",
                "url":"id/<teamId>/joinString/",
                "type": "protected",
                "method": "GET",
                "descr": "Generates join string for team."
            },
            {
                "name": "join",
                "url": "id/<teamId>/join/<joinString>/",
                "type": "protected",
                "method": "POST",
                "descr": "Attempts to join team."
            },
            {
                "name": "kick",
                "url": "id/<teamId>/kick/<userId>/",
                "type": "protected",
                "method": "POST",
                "descr": "Kicks someone or yourself (<userId>=`@me`) from team."
            },
            {
                "name": "list",
                "url": "list/<userId>/",
                "type": "public",
                "method": "",
                "descr": "Lists teams for user or yourself (<userId>=`@me`)."
            },
        ], 200

teamRoutes = [(TeamDescr, '/'), (createTeam, '/create/'), (Team, '/id/<teamId>/'), (TeamJoinstring, '/id/<teamId>/joinString/'), (Join, '/id/<teamId>/join/<joinString>/'), (Kick, '/id/<teamId>/kick/<userId>/'), (ListParticipatingTeam, '/list/participating/<gameId>/'), (ListTeam, '/list/<userId>/')]