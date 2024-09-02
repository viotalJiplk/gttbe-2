from flask_restx import Resource
from shared.models import SchoolsModel
from utils import AuthResult, hasPermissionDecorator
from shared.utils import perms
from typing import List

class Schools(Resource):
    @hasPermissionDecorator([perms.school.listAll], False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all schools

        Returns:
            dict: List of schools
        """
        return {"schools": SchoolsModel.listSchools()}
