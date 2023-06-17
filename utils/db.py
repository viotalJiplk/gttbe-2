from config import config
import mysql.connector
from functools import wraps

def getConnection(autocommit = True):
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

def fetchAllWithNames(cursor):
    columns = cursor.description 
    return [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

def dbConn(autocommit: bool = True, buffered: bool = True):
    def wrapper(func):
        @wraps(func)
        def connection(*args, **kwargs):
            db = getConnection(autocommit)
            cursor = db.cursor(buffered)
            result = func(cursor=cursor, db=db, *args, **kwargs)
            cursor.close()
            db.close()
            return result
        return connection
    return wrapper
