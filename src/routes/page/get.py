from flask_restx import Resource
from shared.models.page import PageModel
from utils.jws import AuthResult
from utils.permissions import hasPermissionDecorator
from shared.utils.permissionList import perms
from utils.error import ReturnableError
from utils.errorList import errorList
from typing import List

class Page(Resource):
    @hasPermissionDecorator([perms.page.read], False)
    def get(self, name, authResult: AuthResult, permissions: List[str]):
        """Gets a page

        Args:
            name (str): name of the page

        Returns:
            dict: name and content of the page
        """
        page = PageModel.getById(name)
        if page is None :
            raise errorList.data.doesNotExist
        return {
            "name": page.name,
            "value": page.value
        }, 200
