from flask_restx import Resource
from .stage import Stages, StageCreate, StageListAll
from .matchesList import MatchesList

stageRoutes = [(StageCreate, '/create'), (Stages, '/<stageId>/'), (MatchesList, '/<stageId>/matches/'), (StageListAll, '/listAll/')]
