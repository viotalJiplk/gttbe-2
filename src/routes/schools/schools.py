from flask_restx import Resource
from models.school import SchoolsModel

class Schools(Resource):
    def get(self):
        """Lists all schools

        Returns:
            dict: List of schools
        """
        return {"schools": SchoolsModel.listSchools()}
