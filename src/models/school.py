from utils.db import fetchAllWithNames, dbConn
from utils.objectDbSync import ObjectDbSync

class SchoolsModel(ObjectDbSync):
    tableName = "schools"
    tableId = "schoolId"

    def __init__(self, name=None, schoolId=None):
        self.schoolId = schoolId
        self.name = name

    @classmethod
    @dbConn()
    def listSchools(cls, cursor, db):
        cursor.execute("SELECT schoolId, name from schools ORDER BY schoolId")
        return fetchAllWithNames(cursor)
