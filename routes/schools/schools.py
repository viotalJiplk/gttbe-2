from flask_restful import Resource
from models.school import SchoolsModel

class Schools(Resource):
    def get(self):
        return {"schools": SchoolsModel.listSchools()}
