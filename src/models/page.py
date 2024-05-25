from utils.db import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date

class PageModel:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return json.dumps({
            "name": self.name,
            "value": self.value
        })

    @classmethod
    @dbConn()
    def getByName(cls, name, cursor, db):
        sql = "SELECT * FROM `page` WHERE name=%(name)s"
        cursor.execute(sql, {'name': name})
        row = fetchOneWithNames(cursor)
        if row is None:
            return None
        return PageModel(name=row['name'], value=row['value'])
