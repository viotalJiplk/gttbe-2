from os import environ, getenv

config = {
    'host': environ["DBhost"],
    'user': environ["DBuser"],
    'password': environ["DBpass"],
    'database': environ["DBdb"]
}
selfref = {
    'root_url': environ["root_url"]
}
discord = {
    'client_id': environ["client_id"],
    'client_secret': environ["client_secret"],
    'api_endpoint': environ["api_endpoint"],
    'state_ttl': int(environ["state_ttl"]),
    'token_ttl': int(environ["token_ttl"]),
    'userid_claim': environ["userid_claim"],
}

production = not (getenv("PROD") is None or getenv("PROD")=="no")