from utils.db import fetchAllWithNames, dbConn

class SchoolsModel:
    def __init__(self, name=None, schoolId=None):        
        self.schoolId = schoolId
        self.name = name
    
    @classmethod
    @dbConn()
    def listSchools(cls, cursor, db):
        cursor.execute("SELECT schoolId, name from schools ORDER BY schoolId")
        return fetchAllWithNames(cursor)