from utils.db import getConnection
import datetime
import requests
from config import discord
from Crypto.Random import random

def getuserobject(access_token):
    headers = {
        "Authorization": "Bearer " + access_token
    }
    try:
        r = requests.get('%s/oauth2/@me' % discord['api_endpoint'], headers=headers)
    except Exception as e:
        return {"state": 1, "msg": "discord /oauth2/@me error: " + e.args[0]}
        #discord token endpoint error
    if(r.status_code != 200):
        return {"state": 1, "msg": "discord /oauth2/@me responded: " + str(r.status_code) + r.text}
        #discord token endpoint error
    return r.json()

def insertTokens(token_response, userid):
    values = {
        'userid': userid,
        'refresh_token': token_response["refresh_token"],
        'access_token': token_response["access_token"],
        'expires_in': datetime.datetime.now() + datetime.timedelta(0,token_response["expires_in"])
    }

    try:
        db = getConnection(autocommit=True)
    except:
        return {"state": 1, "msg": "Cannot connect to database"}
    cursor = db.cursor(buffered=True)
    try:
        query = "INSERT INTO users (`userid`, `access_token`, `refresh_token`, `expires_in`) VALUES (%(userid)s, %(access_token)s, %(refresh_token)s, %(expires_in)s);"
        cursor.execute(query, values)
    except Exception as e:
        try:
            query = "UPDATE users SET `refresh_token` = %(refresh_token)s, `access_token` = %(access_token)s, `expires_in` = %(expires_in)s WHERE `userid` = %(userid)s;"
            cursor.execute(query, values)
        except Exception as e:
            cursor.close()
            db.close()
            return {"state": 1, "msg": "Cannot insert tokens to database"}
    cursor.close()
    db.close()
    return 200

def genState():
    """ Generate a 100-char alnum string. 190 bits of entropy. """
    alnum = ''.join(c for c in map(chr, range(256)) if c.isalnum())
    return ''.join(random.choice(alnum) for _ in range(100))

def insertState():
    state = genState()
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