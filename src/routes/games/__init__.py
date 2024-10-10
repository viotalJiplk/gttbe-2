from .games import Games, GamePage, CreateGame
from flask_restx import Resource

gameRoutes = [(Games, '/<gameId>/'), (GamePage, '/<gameId>/page/'), (CreateGame, '/create')]
