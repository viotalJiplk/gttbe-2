import datetime
from utils.db import dbConn
import logging
from utils.generator import genState
from config import discord


class StateModel:

    def __init__(self, state: str, date):
        self.state = state
        self.date = date

    @classmethod
    @dbConn(autocommit =True, buffered=True)
    def create(cls, cursor, db):
        state = genState(200)
        date = datetime.datetime.now() + datetime.timedelta(0,discord['state_ttl'])
        query = "INSERT INTO `states` (`state`, `date`) VALUES (%(state)s, %(date)s);"
        cursor.execute(query, {'state': state,'date': date})
        return cls(state=state, date=date)

    @classmethod
    @dbConn(autocommit=True, buffered=True)
    def testAndDelete(cls, state: str, cursor, db):
        query = "DELETE FROM states WHERE `state` = %(state)s;"
        cursor.execute(query, {'state': state})
        
        if cursor.rowcount == 1:
            return True
        elif cursor.rowcount > 1:
            logging.warning("DB: The state was not unique.")

        return False