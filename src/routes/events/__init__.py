from flask_restx import Resource
from .events import EventList, EventCreate, Events
from .matchesAll import MatchesList

eventRoutes = [(EventList, '/list'), (EventCreate, '/create'), (MatchesList, '/<eventId>/listMatches/'), (Events, '/<eventId>/')]
