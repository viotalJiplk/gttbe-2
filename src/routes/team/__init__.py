from flask_restx import Resource
from routes.team.create import createTeam
from routes.team.list import ListTeam, ListParticipatingTeam
from routes.team.id import Team, TeamJoinstring, Join, Kick

teamRoutes = [(createTeam, '/create/'), (Team, '/id/<teamId>/'), (TeamJoinstring, '/id/<teamId>/joinString/'), (Join, '/id/<teamId>/join/<joinString>/'), (Kick, '/id/<teamId>/kick/<userId>/'), (ListParticipatingTeam, '/list/participating/<gameId>/<withDiscord>/'), (ListTeam, '/list/<userId>/')]
