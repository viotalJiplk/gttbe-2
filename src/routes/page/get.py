from flask_restful import Resource, request
from models.page import PageModel
from utils.jws import jwsProtected

class Page(Resource):
    def get(self, name):
        page = PageModel.getByName(name)
        if(page == None):
            return {"kind":"Page", "msg": "Page not found."}, 404
        return {
            "name": page.name,
            "value": page.value
        }, 200