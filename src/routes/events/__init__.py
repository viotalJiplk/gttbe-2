from routes.discord.auth import Auth, TokenEndpoint
from flask_restx import Resource
from routes.events.events import EventList, EventCreate, Events
from routes.events.matchesAll import MatchesList

eventRoutes = [(EventList, '/list'), (EventCreate, '/create'), (MatchesList, '/<eventId>/listMatches/'), (Events, '/<eventId>/')]
