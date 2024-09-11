from jwcrypto import jwk, jws
from jwcrypto.common import json_encode, json_decode
from jwcrypto.jws import InvalidJWSObject, InvalidJWSSignature
from functools import wraps
from flask_restful import request
from shared.utils import config
from .errorListFile import errorList
import time
import json
from .error import ReturnableError, handleReturnableError
from .nsForDecorators import blankNs
from .others import returnError

key = jwk.JWK.generate(kty='RSA', size=2048)
private = key.export_private()
public = key.export_public()

def generateJWS(claims):
    """Generates json web token signed

    Args:
        claims (dict): dict of things to sign

    Returns:
        str: json web token signed
    """
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
    """Verifies and decodes json web token signed

    Args:
        jwsin (str): json web token signed
    Raises:
        InvalidJWSObject: invalid son web token signed
        InvalidJWSSignature : invalid signature
    Returns:
        dict: payload of token
    """
    jwstoken = jws.JWS()
    jwstoken.deserialize(jwsin, key)
    # jwstoken.verify(key)
    return jwstoken.payload

class AuthResult:
    """Auth result representation"""
    def __init__(self, userId, payload):
        """Initialize auth result representation

        Args:
            userId (_type_): _description_
            payload (_type_): _description_
        """
        self.userId = userId
        self.payload = payload

def getAuth(headers):
    """Try authenticating from http headers

    Args:
        headers (List[str]): httpHeaders

    Raises:
        errorList.jws.missingAuthHeader: When missing auth header
        errorList.jws.invalidToken: When token is invalid
        errorList.jws.InvalidSignature: When signature is invalid
        errorList.jws.expired: When signature expired
        errorList.jws.untrusted: When signature is untrusted
        errorList.jws.missingUserId: When signature is missing userId in payload
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
        raise errorList.jws.InvalidSignature
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
    errors = [errorList.jws.invalidToken, errorList.jws.InvalidSignature, errorList.jws.expired, errorList.jws.untrusted, errorList.jws.missingUserId]
    if not optional:
        errors.append(errorList.jws.missingAuthHeader)
    def wrapper(func):
        @wraps(func)
        @blankNs.doc(security="jws")
        @handleReturnableError
        @returnError(errors)
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
