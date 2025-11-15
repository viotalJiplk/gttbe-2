from flask_restx import Resource
from .create import createTeam
from .list import ListParticipatingTeamsWithPlayers, ListParticipatingTeamsWithPlayersAdmin
from .id import Team, TeamJoinstring, Join, Kick

teamRoutes = [(createTeam, '/create/'), (Team, '/id/<teamId>/'), (TeamJoinstring, '/id/<teamId>/joinString/'), (Join, '/id/<teamId>/join/<joinString>/'), (Kick, '/id/<teamId>/kick/<userId>/'), (ListParticipatingTeamsWithPlayers, '/list/participating/<gameId>/players/'), (ListParticipatingTeamsWithPlayersAdmin, '/list/participating/<gameId>/players/admin/<withDiscord>/')]
