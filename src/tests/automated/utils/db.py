from .config import config
from mysql.connector import connect

def getConnection(autocommit = True):
    db = connect(
        host=config.db.host,
        user=config.db.user,
        password=config.db.password,
        database=config.db.database,
        charset='utf8mb4',
        collation='utf8mb4_czech_ci',
        use_unicode=True,
        autocommit=autocommit
    )
    return db
