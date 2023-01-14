from flask_restful import Resource, request
from routes.discord.jws import generateJWS


class Test(Resource):
    def get(self):

        return generateJWS({"test":1})