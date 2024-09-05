from flask_restx import Resource
from .events import EventList, EventCreate, Events
from .matchesAll import MatchesList
from .stagesList import StagesList

eventRoutes = [(EventList, '/listAll'), (EventCreate, '/create'), (MatchesList, '/<eventId>/matches/'), (StagesList, '/<eventId>/stages/'), (Events, '/<eventId>/')]
