from flask_restx import Resource
from .matches import Matches, MatchCreate, MatchListAll

matchRoutes = [(MatchCreate, '/create/'), (Matches, '/<matchId>/'), (MatchListAll, '/listAll/')]
