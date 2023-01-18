from flask_restful import Resource
from utils.db import getConnection

class Schools(Resource):
    def get(self):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        cursor.execute("SELECT id, name from schools")
        schools = cursor.fetchall()
        cursor.close()
        db.close()
        
        return {"schools": schools}
