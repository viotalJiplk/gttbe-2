from config import config
import mysql.connector

def getConnection(autocommit=True):
    db = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database'],
        autocommit=autocommit
    )
    return db