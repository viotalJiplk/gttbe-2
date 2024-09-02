from flask_restx import Resource
from shared.models.page import PageModel
from utils import AuthResult, hasPermissionDecorator, ReturnableError, errorList
from shared.utils import perms
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
