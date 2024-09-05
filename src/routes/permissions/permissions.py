from flask_restx import Resource
from shared.models import PermissionModel
from utils import AuthResult, hasPermissionDecorator
from shared.utils import perms
from typing import List

class Permissions(Resource):
    @hasPermissionDecorator([perms.permission.listAll], False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all schools

        Returns:
            dict: List of schools
        """
        return PermissionModel.listAll()
