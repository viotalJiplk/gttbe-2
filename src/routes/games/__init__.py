from .games import Games, GamePage, CreateGame

gameRoutes = [(Games, '/<gameId>/'), (GamePage, '/<gameId>/page/'), (CreateGame, '/create')]
