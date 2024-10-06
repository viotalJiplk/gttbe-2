import json
from os import environ, getenv

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
    """Database config

    Attributes:
            host (str): database host
            user (str): database username
            password (str): database password
            database (str): database name
    """
    def  __init__(self, defaultsList: dict):
        """ Initializes Database config.

        Args:
            defaultsList (dict): dict with default values
        """
        self.host = checkEnvVariable("DBhost", defaultsList["host"])
        self.user = checkEnvVariable("DBuser", defaultsList["user"])
        self.password = checkEnvVariable("DBpass", defaultsList["password"])
        self.database = checkEnvVariable("DBdb", defaultsList["database"])

    def toDict(self):
        """returns dict representation of object"""
        return{
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "database": self.database,
        }
    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

class Selfref:
    """Self reference config

    Attributes:
            root_url (str): root url of server
    """
    def  __init__(self, defaultsList: dict):
        """ Initializes reference config.
        Args:
            defaultsList (dict): dict with default values
        """
        self.root_url = checkEnvVariable("root_url", defaultsList["root_url"])

    def toDict(self):
        """returns dict representation of object"""
        return{
            "root_url": self.root_url
        }

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

class Discord:
    """Discord config

    Attributes:
            redir_url (str): discord redirect url
            client_id (str): discord client id
            client_secret (str): discord client secret
            api_endpoint (str): discord api endpoint url
            state_ttl (str): unique state time to live
            token_ttl (str): json web token time to live
            userid_claim (str): user claim name in json web token
    """
    def  __init__(self, defaultsList: dict, selfref: Selfref):
        self.redir_url = selfref.root_url + checkEnvVariable("redir_url", defaultsList["redir_url"])
        self.client_id = checkEnvVariable("client_id", defaultsList["client_id"])
        self.client_secret = checkEnvVariable("client_secret", defaultsList["client_secret"])
        self.api_endpoint = checkEnvVariable("api_endpoint",defaultsList["api_endpoint"])
        self.state_ttl = int(checkEnvVariable("state_ttl", defaultsList["state_ttl"]))
        self.token_ttl = int(checkEnvVariable("token_ttl", defaultsList["token_ttl"]))
        self.userid_claim = selfref.root_url + checkEnvVariable("userid_claim", defaultsList["userid_claim"])

    def toDict(self):
        """returns dict representation of object"""
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
    """Config of the application

    Attributes:
            db (Db): Database config
            selfref (Selfref): self reference config
            discord (Discord): discord config
            production (bool): is instance production
    """
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
                cls.dynamicFileFolder = str(checkEnvVariable("DYNFOLDER", defaults["dynamicFileFolder"]))
        return cls._instance

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        return {
            "db": self.db.toDict(),
            "selfref": self.selfref.toDict(),
            "discord": self.discord.toDict(),
            "production": self.production
        }

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4)

config = Config()
