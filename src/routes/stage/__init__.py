from routes.discord.auth import Auth, TokenEndpoint
from flask_restx import Resource
from routes.stage.stage import Stages, StageCreate

stageRoutes = [(StageCreate, '/create'), (Stages, '/<stageId>/')]
