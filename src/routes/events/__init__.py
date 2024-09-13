from flask_restx import Resource
from .events import EventList, EventCreate, Events
from .matchesAll import MatchesListFromEvent
from .stagesList import StagesList

eventRoutes = [(EventList, '/listAll'), (EventCreate, '/create'), (MatchesListFromEvent, '/<eventId>/matches/'), (StagesList, '/<eventId>/stages/'), (Events, '/<eventId>/')]
