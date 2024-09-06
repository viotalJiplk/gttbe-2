from ..utils import fetchAllWithNames, dbConn
from ..utils import ObjectDbSync

class SchoolsModel(ObjectDbSync):
    """Representation of schools

    Attributes:
            schoolId (int): id of school
            schoolName (str): name of school
    """
    tableName = "schools"
    tableId = "schoolId"

    def __init__(self, name=None, schoolId=None):
        """Initializes representation of schools

            Attributes:
                    schoolId (int): id of school
                    schoolName (str): name of school
        """
        self.schoolId = schoolId
        self.name = name
        super().__init__()

    @classmethod
    @dbConn()
    def listSchools(cls, cursor, db):
        """Lists all schools

        Returns:
            list[dict]: list of dict of schools (value = column name)
        """
        cursor.execute("SELECT schoolId, name from schools ORDER BY schoolId")
        return fetchAllWithNames(cursor)
