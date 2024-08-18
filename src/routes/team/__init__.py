from flask_restx import Resource
from .create import createTeam
from .list import ListParticipatingTeam
from .id import Team, TeamJoinstring, Join, Kick

teamRoutes = [(createTeam, '/create/'), (Team, '/id/<teamId>/'), (TeamJoinstring, '/id/<teamId>/joinString/'), (Join, '/id/<teamId>/join/<joinString>/'), (Kick, '/id/<teamId>/kick/<userId>/'), (ListParticipatingTeam, '/list/participating/<gameId>/<withDiscord>/')]
