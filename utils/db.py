from config import config
import mysql.connector

def getConnection(autocommit=True):
    db = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database'],
        charset='utf8mb4',
        collation='utf8mb4_czech_ci',
        use_unicode=True,
        autocommit=autocommit
    )
    return db