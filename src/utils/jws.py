from jwcrypto import jwk, jws
from jwcrypto.common import json_encode, json_decode
from jwcrypto.jws import InvalidJWSObject, InvalidJWSSignature, JWKeyNotFound
from functools import wraps
from flask_restful import request
from shared.utils import config
from .errorListFile import errorList
import time
import json
from .error import ReturnableError, handleReturnableError
from .nsForDecorators import blankNs
from .others import returnError
from datetime import datetime, timezone, timedelta
from json import loads
from cryptography.hazmat.primitives.hashes import SHA1, SHA256
from .keystore import KeyStore, UseTypes

from typing import List, Union

sigKeyStore = KeyStore(UseTypes.sig, timedelta(days=1),timedelta(minutes=30))
sigKeyStore.update()

def generateJWS(claims, subjectIdentifier: str, aud: list[str], authTime: datetime, nonce: str):
    """Generates json web token signed

    Args:
        claims (dict): dict of things to sign

    Returns:
        str: json web token signed
    """
    payload = {
        "iss": config.selfref.root_url,
        "sub": subjectIdentifier,
        "aud": aud,
        "exp": int(time.time()) + config.discord.token_ttl,
        "iat": int(time.time()),
        "auth_time": int(authTime.timestamp()),
        "nonce": nonce
    }
    payload = payload | claims
    payload = json_encode(payload)
    jwstoken = jws.JWS(payload.encode('utf-8'))
    sigKeyStore.update()
    key = sigKeyStore.getFirstActiveKey()
    jwstoken.add_signature(key.key, None, json_encode({"alg": key.alg, "kid": key.kid}))
    return jwstoken.serialize(True)

def verifyJWS(jwsin):
    """Verifies and decodes json web token signed

    Args:
        jwsin (str): json web token signed
    Raises:
        InvalidJWSObject: invalid son web token signed
        InvalidJWSSignature : invalid signature
        jwcrypto.common.JWKeyNotFound :
    Returns:
        dict: payload of token
    """
    jwstoken = jws.JWS()
    sigKeyStore.update()
    jwstoken.deserialize(jwsin, sigKeyStore.getKeyset())
    # jwstoken.verify(key)
    return jwstoken.payload

class AuthResult:
    """Auth result representation"""
    def __init__(self, userId: str, issuer: str, subjectIdentifier: str, audience: list[str], expiration: datetime, issuedAt: datetime, authTime: datetime, nonce: str, payload: dict):
        """Initialize auth result representation

        Args:
            userId (str): discord user id of user
            issuer (str): issuer of the authentication
            subjectIdentifier(str): unique id of the subject of authorization SHOULD be equivalent of userId
            audience(list[str]): intended audience(s)
            expiration(datetime): Expiration time of login
            issuedAt(datetime): when this auth token was issued
            authTime(datetime): time of the authentication of the user
            nonce(str): unique request string
            payload (dict): whole payload of the jwt
        """
        self.userId = userId
        self.issuer = issuer
        self.subjectIdentifier = subjectIdentifier # unique identifier of the user
        self.audience = audience # audience of the authentication
        self.expiration = expiration
        self.issuedAt = issuedAt
        self.authTime = authTime
        self.nonce = nonce
        self.payload = payload

    @classmethod
    def fromDict(cls, payload: dict) -> Union[None, "AuthResult"]:
        """Creates Class from dictionary

        Args:
            payload (dict): input dictionary
        """
        def getTimestamp(anything):
            if not isinstance(anything, int):
                return None
            else:
                return datetime.fromtimestamp(anything, timezone.utc)

        if not isinstance(payload, dict):
            return None

        if not (("iss" in payload) and ("sub" in payload) and ("aud" in payload) and ("exp" in payload) and ("iat" in payload) and ("auth_time" in payload) and ("nonce" in payload)):
            return None

        if not isinstance(payload["iss"], str):
            return None

        if not isinstance(payload["sub"], str):
            return None

        if not isinstance(payload["aud"], list):
            return None
        else:
            for aud in payload["aud"]:
                if not isinstance(aud, str):
                    return None

        payload["exp"] = getTimestamp(payload["exp"])
        if not isinstance(payload["exp"], datetime):
            return None

        payload["iat"] = getTimestamp(payload["iat"])
        if not isinstance(payload["iat"], datetime):
            return None

        payload["auth_time"] = getTimestamp(payload["auth_time"])
        if not isinstance(payload["auth_time"], datetime):
            return None

        if not isinstance(payload["nonce"], str):
            return None

        return cls(payload["sub"], payload["iss"], payload["sub"], payload["aud"], payload["exp"], payload["iat"], payload["auth_time"], payload["nonce"], payload)

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
        errorList.jws.malformedToken: When there is required field missing in payload
        errorList.jws.issuedInFuture: When auth or iat is in future
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
    except JWKeyNotFound:
        raise errorList.jws.InvalidSignature

    result = AuthResult.fromDict(json_decode(result))
    if result is None:
        raise errorList.jws.invalidToken

    if(int(result.expiration.timestamp()) <= int(time.time())):
        raise errorList.jws.expired
    if(int(result.authTime.timestamp()) > int(time.time())):
        raise errorList.jws.issuedInFuture
    if(int(result.issuedAt.timestamp()) > int(time.time())):
        raise errorList.jws.issuedInFuture
    if(result.issuer != config.selfref.root_url):
        raise errorList.jws.untrusted

    return result


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
    errors = [errorList.jws.invalidToken, errorList.jws.InvalidSignature, errorList.jws.expired, errorList.jws.untrusted, errorList.jws.missingUserId, errorList.jws.malformedToken, errorList.jws.issuedInFuture, errorList.jws.wrongAudience]
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
                if "backend" not in result.audience:
                    raise errorList.jws.wrongAudience
            except ReturnableError as e:
                if e == errorList.jws.missingAuthHeader and optional:
                    return func(authResult = None, *args, **kwargs)
                else:
                    raise
            return func(authResult = result, *args, **kwargs)
        return wrappedGetAuth
    return wrapper
