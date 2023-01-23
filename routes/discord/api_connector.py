from utils.db import getConnection
import datetime
import requests
from config import discord
from utils.generator import genState


def insertState():
    state = genState(200)
    try:
        db = getConnection(autocommit=True)
    except:
        return {"state": 1, "msg": "Cannot connect to database"}
    cursor = db.cursor(buffered=True)
    try:
        query = "INSERT INTO `states` (`state`, `date`) VALUES (%(state)s, %(date)s);"
        cursor.execute(query, {'state': state,'date': datetime.datetime.now() + datetime.timedelta(0,discord['state_ttl'])})
    except Exception as e:
        cursor.close()
        db.close()
        return {"state": 1, "msg": "Cannot insert state to database"}
    cursor.close()
    db.close()
    return state

def testState(state):
    try:
        db = getConnection(autocommit=True)
    except:
        return False
    cursor = db.cursor(buffered=True)
    try:
        query = "SELECT 1 FROM states WHERE `state` = %(state)s AND `date` >= %(date)s;"
        cursor.execute(query, {'state': state,'date': datetime.datetime.now()})
        if(cursor.rowcount != 1):
            cursor.close()
            db.close()
            return False
        query = "DELETE FROM states WHERE `state` = %(state)s;"
        cursor.execute(query, {'state': state})
    except Exception as e:
        cursor.close()
        db.close()
        return False
    cursor.close()
    db.close()
    return True