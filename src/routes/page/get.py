from flask_restx import Resource
from models.page import PageModel
from utils.jws import jwsProtected

class Page(Resource):
    def get(self, name):
        """Gets a page

        Args:
            name (str): name of the page

        Returns:
            dict: name and content of the page
        """
        page = PageModel.getById(name)
        if(page == None):
            return {"kind":"Page", "msg": "Page not found."}, 404
        return {
            "name": page.name,
            "value": page.value
        }, 200
