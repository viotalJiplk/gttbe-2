from flask_restx import Resource
from shared.models import SchoolsModel
from utils import AuthResult, hasPermissionDecorator, returnParser, postJsonParse
from shared.utils import perms
from typing import List

createAttributes = {
    "name": [str]
}

class SchoolsList(Resource):
    @returnParser({"schoolId": [int], "name": [str]}, 200, True, False)
    @hasPermissionDecorator([perms.school.listAll], False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all schools

        Returns:
            dict: List of schools
        """
        return SchoolsModel.listSchools()

class Schools(Resource):
    @returnParser({"schoolId": [int], "name": [str]}, 200, True, False)
    @postJsonParse(createAttributes)
    @hasPermissionDecorator([perms.school.create], False)
    def post(self, data, authResult: AuthResult, permissions: List[str]):
        return SchoolsModel.create(data["name"]).toDict()
