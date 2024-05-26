import json
from os import environ, getenv

def toBool(value: str)-> bool:
    if(type(value) == str):
        return value.lower() == "yes" or value.lower() == "true"
    else:
        value == True

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

class Selfref:
    def  __init__(self, defaultsList):
        self.root_url = checkEnvVariable("root_url", defaultsList["root_url"])

    def toDict(self):
        return{
            "root_url": self.root_url
        }

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

class Discord:
    def  __init__(self, defaultsList, selfref: Selfref):
        self.redir_url = selfref.root_url + checkEnvVariable("redir_url", defaultsList["redir_url"])
        self.client_id = checkEnvVariable("client_id", defaultsList["client_id"])
        self.client_secret = checkEnvVariable("client_secret", defaultsList["client_secret"])
        self.api_endpoint = checkEnvVariable("api_endpoint",defaultsList["api_endpoint"])
        self.state_ttl = int(checkEnvVariable("state_ttl", defaultsList["state_ttl"]))
        self.token_ttl = int(checkEnvVariable("token_ttl", defaultsList["token_ttl"]))
        self.userid_claim = selfref.root_url + checkEnvVariable("userid_claim", defaultsList["userid_claim"])

    def toDict(self):
        return{
            "redir_url": self.redir_url,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "api_endpoint": self.api_endpoint,
            "state_ttl": self.state_ttl,
            "token_ttl": self.token_ttl,
            "userid_claim": self.userid_claim,
        }

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

class Config(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            # Put any initialization here.
            with open('config.json') as f:
                defaults = json.load(f)
                cls.db = Db(defaults["db"])
                cls.selfref = Selfref(defaults["selfref"])
                cls.discord = Discord(defaults["discord"], cls.selfref)
                cls.production = toBool(checkEnvVariable("PROD", defaults["production"]))
        return cls._instance

    def toDict(self):
        return {
            "db": self.db.toDict(),
            "selfref": self.selfref.toDict(),
            "discord": self.discord.toDict(),
            "production": self.production
        }

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

config = Config()
