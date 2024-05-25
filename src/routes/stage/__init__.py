from routes.discord.auth import Auth, TokenEndpoint
from flask_restful import Resource, request
from routes.stage.stage import Stages, StageCreate

class StageDescr(Resource):
    def get(self):
        return [
            {
                "name": "list",
                "url": "list/",
                "type": "public",
                "method": "GET",
                "descr": "Gets all stages."
            }
        ], 200

stageRoutes = [(StageDescr, '/'), (StageCreate, '/create'), (Stages, '/<stageId>/')]
