from utils.db import getConnection

class TeamModel:
    def __init__(self, name = "", gameId = None):
        self.name = name
        self.gameId = gameId

    def json(self):
        return {'name': self.name, 'game': self.game}

    def insert(self):
        db = getConnection(autocommit=False)
        cursor = db.cursor(buffered=True)
        query = "INSERT INTO teams (name, game) VALUES (%s, %s)"
        values = (self.name, self.game)
        cursor.execute(query, values)
        cursor.close()
        db.close()

    @classmethod
    def find_id_by_name(cls, name):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        query = "SELECT teamId from teams WHERE name=%s"
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        cursor.close()
        db.close()
        if row:
            return row[0]
        else:
            return None