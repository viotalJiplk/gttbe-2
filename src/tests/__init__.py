from flask import send_from_directory
from flask_restful import Resource, request

class TestPages(Resource):
    def get(self, content):
        return send_from_directory('tests/testpages', content)

testRoutes = [(TestPages, '/testpages/<path:content>')]
