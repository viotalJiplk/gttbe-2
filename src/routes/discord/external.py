from flask_restx import Resource
from utils import keys

class PublicKeys(Resource):
    def get(self):
        """
            Returns public keys
        Returns:
            dict: keys
        """

        return keys.keysInfo(), 200
        # could technically throw error if state is not unique
