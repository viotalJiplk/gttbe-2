from flask_restx import Resource
from shared.models import SchoolsModel
from utils import AuthResult, hasPermissionDecorator, returnParser
from shared.utils import perms
from typing import List

class Schools(Resource):
    @returnParser({"schoolId": [int], "name": [str]}, 200, True, False)
    @hasPermissionDecorator([perms.school.listAll], False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all schools

        Returns:
            dict: List of schools
        """
        return SchoolsModel.listSchools()
