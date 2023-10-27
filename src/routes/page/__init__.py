from routes.page.get import Page
from flask_restful import Resource, request

class PageDescr(Resource):
    def get(self):
        return [
            {
                "get": "get",
                "url": "/<name>/",
                "type": "public",
                "method": "GET",
                "descr": "Get page."
            },
        ], 200

pageRoutes = [(PageDescr, '/'), (Page, "/<name>/")]