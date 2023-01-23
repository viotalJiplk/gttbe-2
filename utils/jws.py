from jwcrypto import jwk, jws
from jwcrypto.common import json_encode
from config import selfref, discord
import time

key = jwk.JWK.generate(kty='RSA', size=2048)
private = key.export_private()
public = key.export_public()

def generateJWS(claims):
    payload = {
        "iss": selfref["root_url"],
        "exp": int(time.time()) + discord["token_ttl"]
    }
    payload = payload | claims
    payload = json_encode(payload)
    jwstoken = jws.JWS(payload.encode('utf-8'))
    jwstoken.add_signature(key, None, json_encode({"alg": "RS512"}), json_encode({"kid": key.thumbprint()}))
    return jwstoken.serialize(True)

def verifyJWS(jws):
    jwstoken = jws.JWS()
    jwstoken.deserialize(sig)
    jwstoken.verify(key)
    return jwstoken.payload