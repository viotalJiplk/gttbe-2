from flask_restx import Resource
from shared.models.school import SchoolsModel
from utils.jws import AuthResult
from utils.permissions import hasPermissionDecorator
from shared.utils.permissionList import perms
from utils.error import ReturnableError
from utils.errorList import errorList
from typing import List

class Schools(Resource):
    @hasPermissionDecorator([perms.school.listAll], False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all schools

        Returns:
            dict: List of schools
        """
        return {"schools": SchoolsModel.listSchools()}
