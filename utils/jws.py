from jwcrypto import jwk, jws
from jwcrypto.common import json_encode, json_decode
from config import selfref, discord
import time
import json

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

def verifyJWS(jwsin):
    jwstoken = jws.JWS()
    jwstoken.deserialize(jwsin, key)
    # jwstoken.verify(key)
    return jwstoken.payload

def authorize(request):
    if(request.headers["Authorization"] == None):
        raise Exception("Missing Authorization header!")
    result = verifyJWS(request.headers["Authorization"].split(" ")[1])
    result = json_decode(result)
    if(result["exp"] <= int(time.time())):
        raise Exception("Expired!")
    if(result["iss"] != selfref["root_url"]):
        raise Exception("Untrusted issuer!")
    if(result[discord["userid_claim"]] == None):
        raise Exception("Missing userid!")
    return {"userId": result[discord["userid_claim"]], "payload": result}
