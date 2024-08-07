from .attributesObserver import AttributesObserver
from .db import dbConn, fetchOneWithNames, fetchAllWithNames

class ObjectDbSync(AttributesObserver):
    def __init__(self):
        if not hasattr(self, "tableId"):
            raise Exception("Missing required tableId.")
        if not hasattr(self, "tableName"):
            raise Exception("Missing required tableName.")
        super().__init__()
        self.register(self.update, None, "update")

    @dbConn()
    def update(self, name, value, cursor, db):
        query = f"UPDATE `{self.tableName}` SET `{name}` = %s WHERE `{self.tableId}` = %s;"
        cursor.execute(query, (value, getattr(self, self.tableId)))

    @dbConn()
    def delete(self, cursor, db):
        query = f"DELETE FROM `{self.tableName}` WHERE `{self.tableId}` = %s;"
        cursor.execute(query, (getattr(self, self.tableId),))

    @classmethod
    @dbConn()
    def getById(cls, tableIdValue, cursor, db):
        query = f"SELECT * FROM `{cls.tableName}` WHERE `{cls.tableId}` = %s;"
        cursor.execute(query, (tableIdValue,))
        row = fetchOneWithNames(cursor)
        if row:
            return cls(**row)
        else:
            return None

    @classmethod
    @dbConn()
    def getAllDict(cls, cursor, db):
        query = f"SELECT * FROM `{cls.tableName}`;"
        cursor.execute(query)
        return fetchAllWithNames(cursor)

