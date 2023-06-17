from jwcrypto import jwk, jws
from jwcrypto.common import json_encode, json_decode
from jwcrypto.jws import InvalidJWSObject, InvalidJWSSignature
from functools import wraps
from flask_restful import request
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

def jwsProtected(optional: bool = False):
    def wrapper(func):
        def getAuth(*args, **kwargs):
            if "Authorization" not in request.headers:
                if optional:
                    return func(authResult = None, *args, **kwargs)
                else:     
                    return {"kind": "JWS", "msg": "Missing Authorization header!"}, 401
            try:
                result = verifyJWS(request.headers["Authorization"].split(" ")[1])
            except InvalidJWSObject:
                return {"kind": "JWS", "msg": "Invalid JWS token!"}, 401
            except InvalidJWSSignature:
                return {"kind": "JWS", "msg": "Invalid signature!"}, 401
            result = json_decode(result)
            if(result["exp"] <= int(time.time())):
                return {"kind": "JWS", "msg": "Expired!"}, 401
            if(result["iss"] != selfref["root_url"]):
                return {"kind": "JWS", "msg": "Untrusted issuer!"}, 401
            if(result[discord["userid_claim"]] == None):
                return {"kind": "JWS", "msg": "Missing userid!"}, 401
            return func(authResult = {"userId": result[discord["userid_claim"]], "payload": result}, *args, **kwargs)
        return getAuth
    return wrapper