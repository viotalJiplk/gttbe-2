from flask_restx import Resource
from .stage import Stages, StageCreate, StageListAll
from .matchesList import MatchesListFromStage

stageRoutes = [(StageCreate, '/create'), (Stages, '/<stageId>/'), (MatchesListFromStage, '/<stageId>/matches/'), (StageListAll, '/listAll/')]
