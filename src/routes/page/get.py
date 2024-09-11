from flask_restx import Resource
from shared.models.page import PageModel
from utils import AuthResult, hasPermissionDecorator, ReturnableError, errorList, returnParser, returnError
from shared.utils import perms
from typing import List
from copy import deepcopy

class Page(Resource):
    @returnParser({"name": [str], "value": [str]}, 200, False, False)
    @returnError([errorList.data.doesNotExist])
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
