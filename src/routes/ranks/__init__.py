from .ranks import RankList, RankCreate, Ranks

rankRoutes = [(RankList, '/list/<gameId>/'), (RankCreate, '/create'), (Ranks, '/<rankId>/')]
