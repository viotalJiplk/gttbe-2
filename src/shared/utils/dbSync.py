from .attributesObserver import AttributesObserver
from .db import dbConn, fetchOneWithNames, fetchAllWithNames, DatabaseError
from mysql.connector import IntegrityError
from .configLoader import config
from typing import Union

class ObjectDbSync(AttributesObserver):
    """Class for automatic db syncing objects.
        INITIALIZER OF THIS CLASS MUST BE CALLED
    """
    def __init__(self):
        """Initialization of class for automatic db syncing objects
            THIS INITIALIZER MUST BE CALLED
        Raises:
            Exception: Missing required tableId. - Object must have attribute tableId (with name of table primary key in db) before calling init
            Exception: Missing required tableName. - Object must have attribute tableName (with name of table in db) before calling init
        """
        if not hasattr(self, "tableId"):
            raise Exception("Missing required tableId.")
        if not hasattr(self, "tableName"):
            raise Exception("Missing required tableName.")
        super().__init__()
        self.register(self.__update, None, "update")

    @dbConn()
    def __update(self, name, value, cursor, db):
        """Updates attribute in database. (do not call directly)
        """
        query = f"UPDATE `{self.tableName}` SET `{name}` = %s WHERE `{self.tableId}` = %s;"
        cursor.execute(query, (value, getattr(self, self.tableId)))

    @dbConn()
    def delete(self, cursor, db):
        """Deletes object from database.
        Raises:
            DatabaseError: if something still depends on object
        """
        query = f"DELETE FROM `{self.tableName}` WHERE `{self.tableId}` = %s;"
        try:
            cursor.execute(query, (getattr(self, self.tableId),))
        except IntegrityError as e:
            expectedMsg = f'Cannot delete or update a parent row: a foreign key constraint fails (`{config.db.database}`'
            if e.sqlstate == '23000' and e.msg.startswith(expectedMsg):
                raise DatabaseError("Still depends")
            else:
                print(e.msg)
                print(expectedMsg)
                print(e.sqlstate)
                raise

    @classmethod
    @dbConn()
    def getById(cls, tableIdValue:  Union[int, str], cursor, db):
        """Gets object by id.

        Args:
            tableIdValue (Union[int, str]): value of primary key of table

        Returns:
            Union[None, class]: result
        """
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
        """Returns list of dict of all rows in db

        Returns:
            list[dict]: list dict of all rows (key = colum name)
        """
        query = f"SELECT * FROM `{cls.tableName}`;"
        cursor.execute(query)
        return fetchAllWithNames(cursor)

