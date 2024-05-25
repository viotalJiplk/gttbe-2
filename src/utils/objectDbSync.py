from utils.attributesObserver import AttributesObserver
from utils.db import dbConn

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
