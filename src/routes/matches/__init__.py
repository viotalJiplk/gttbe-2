from flask_restx import Resource
from .matches import Matches, MatchCreate

matchRoutes = [(MatchCreate, '/create/'), (Matches, '/<matchId>/')]
