from ..utils import fetchAllWithNames, fetchOneWithNames, dbConn
from json import dumps
from datetime import date
from ..utils import ObjectDbSync
from typing import Union

class PageModel(ObjectDbSync):
    """Representation of page
        Attributes:
            name (str): page name
            value (str): page content
    """
    tableName = "page"
    tableId = "name"

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        super().__init__()

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "name": self.name,
            "value": self.value
        }


    def __str__(self):
        return json.dumps(self.toDict())

    @classmethod
    @dbConn()
    def getByName(cls, name: str, cursor, db):
        """Gets page by name

        Args:
            name (str): name of the page

        Returns:
            Union[PageModel, None]: page
        """
        sql = "SELECT * FROM `page` WHERE name=%(name)s"
        cursor.execute(sql, {'name': name})
        row = fetchOneWithNames(cursor)
        if row is None:
            return None
        return PageModel(name=row['name'], value=row['value'])
