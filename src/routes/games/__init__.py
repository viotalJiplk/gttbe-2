from routes.games.games import Games, GamePage
from flask_restx import Resource

gameRoutes = [(Games, '/<gameId>/'), (GamePage, '/<gameId>/page/')]
