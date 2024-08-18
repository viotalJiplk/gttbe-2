import json
from os import environ, getenv
import os

def toBool(value: str)-> bool:
    if(type(value) == str):
        return value.lower() == "yes" or value.lower() == "true"
    else:
        return value == True

def checkEnvVariable(varName, defaultVAlue) -> str:
    if varName in environ:
        return environ[varName]
    else:
        return defaultVAlue

class Db:
    def  __init__(self, defaultsList):
        self.host = checkEnvVariable("DBhost", defaultsList["host"])
        self.user = checkEnvVariable("DBuser", defaultsList["user"])
        self.password = checkEnvVariable("DBpass", defaultsList["password"])
        self.database = checkEnvVariable("DBdb", defaultsList["database"])

    def toDict(self):
        return{
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "database": self.database,
        }
    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

class Server:
    def  __init__(self, defaultsList):
        self.host = checkEnvVariable("serverHost", defaultsList["host"])
        self.port = checkEnvVariable("serverPort", defaultsList["port"])

    def toDict(self):
        return{
            "host": self.host,
            "port": self.port,
        }
    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)


class Config(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            print(os.getcwd())
            with open('config.json') as f:
                defaults = json.load(f)
                cls.db = Db(defaults["db"])
                cls.server = Server(defaults["server"])
        return cls._instance

    def toDict(self):
        return {
            "db": self.db.toDict(),
        }

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

config = Config()
