from flask_restx import Resource
from shared.models import PermissionModel
from utils import AuthResult, hasPermissionDecorator, returnParser
from shared.utils import perms
from typing import List
from copy import deepcopy

class Permissions(Resource):
    @returnParser([str], 200, True, False)
    @hasPermissionDecorator([perms.permission.listAll], False)
    def get(self, authResult: AuthResult, permissions: List[str]):
        """Lists all Permissions

        Returns:
            dict: List of Permissions
        """
        return PermissionModel.listAll()
