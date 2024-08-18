from flask_restx import Resource
from .stage import Stages, StageCreate

stageRoutes = [(StageCreate, '/create'), (Stages, '/<stageId>/')]
