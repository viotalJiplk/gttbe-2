from jwcrypto import jwk, jws
from jwcrypto.common import json_encode, json_decode
from jwcrypto.jws import InvalidJWSObject, InvalidJWSSignature
from functools import wraps
from flask_restful import request
from shared.utils import config
from .errorList import errorList
import time
import json
from utils.error import ReturnableError, handleReturnableError
from utils.errorList import errorList

key = jwk.JWK.generate(kty='RSA', size=2048)
private = key.export_private()
public = key.export_public()

def generateJWS(claims):
    payload = {
        "iss": config.selfref.root_url,
        "exp": int(time.time()) + config.discord.token_ttl
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

class AuthResult:
    def __init__(self, userId, payload):
        self.userId = userId
        self.payload = payload

def getAuth(headers):
    """Try authenticating from http headers

    Args:
        headers (List[str]): httpHeaders

    Raises:
        ReturnableError: When unable to authenticate

    Returns:
        AuthResult: result of authentication attempt
    """
    if "Authorization" not in headers:
        raise errorList.jws.missingAuthHeader
    try:
        result = verifyJWS(headers["Authorization"].split(" ")[1])
    except InvalidJWSObject:
        raise errorList.jws.invalidToken
    except InvalidJWSSignature:
        raise errorList.jws.missingAuthHeader
    result = json_decode(result)
    if(result["exp"] <= int(time.time())):
        raise errorList.jws.expired
    if(result["iss"] != config.selfref.root_url):
        raise errorList.jws.untrusted
    if(result[config.discord.userid_claim] == None):
        raise errorList.jws.missingUserId
    return AuthResult(result[config.discord.userid_claim], result)

def jwsProtected(optional: bool = False):
    """Decorator that decrypts jws authenticating user

    Args:
        optional (bool, optional): Is authentication optional. (if unable to authenticate authResult = False) Defaults to False.
    Returns:
        callable: The function wrapper.
    Example:
        @jwsProtected()
        def func(authResult: Union[AuthResult, None]):
            #your logic
            pass
    """
    def wrapper(func):
        @wraps(func)
        @handleReturnableError
        def wrappedGetAuth(*args, **kwargs):
            result = None
            try:
                result = getAuth(request.headers)
            except ReturnableError as e:
                if e == errorList.jws.missingAuthHeader and optional:
                    return func(authResult = None, *args, **kwargs)
                else:
                    raise
            return func(authResult = result, *args, **kwargs)
        return wrappedGetAuth
    return wrapper
