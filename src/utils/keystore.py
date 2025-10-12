from jwcrypto import jwk, jws
from cryptography.hazmat.primitives.hashes import SHA1, SHA256
from enum import Enum
from datetime import datetime, timedelta

class KeyType(str, Enum):
    ocy = "oct"
    RSA = "RSA"
    EC = "EC"
    OKP = "OKP"

class UseTypes(str, Enum):
    sig = "sig"
    enc = "enc"

class AlgTypes(str, Enum):
    # HMAC with SHA
    HS256 = "HS256"
    HS384 = "HS384"
    HS512 = "HS512"

    # RSA PKCS#1 v1.5 with SHA
    RS256 = "RS256"
    RS384 = "RS384"
    RS512 = "RS512"

    # RSA-PSS with SHA
    PS256 = "PS256"
    PS384 = "PS384"
    PS512 = "PS512"

    # ECDSA with SHA
    ES256 = "ES256"
    ES384 = "ES384"
    ES512 = "ES512"

    # Edwards Curve
    EdDSA = "EdDSA"

class Key:
    def __init__(self, key: jwk.JWK, kid: str, kty: KeyType, use: UseTypes, alg: AlgTypes, activationTime: datetime|None = None):
        self.key = key
        self.kid = kid
        self.kty = kty
        self.use = use
        self.alg = alg
        self.activationTime = activationTime

    def getSHA1Thumbprint(self):
        return self.key.thumbprint(hashalg=SHA1())

    def getSHA256Thumbprint(self):
        return self.key.thumbprint(hashalg=SHA256())

    def publicInfo(self):
        return {
            "kid": self.kid,
            "kty": self.kty,
            "use": self.use,
            "alg": self.alg,
            "x5t": self.getSHA1Thumbprint(),
            "x5t#S256": self.getSHA256Thumbprint(),
        }

    def toDict():
        return {
            "key": self.key,
            "kid": self.kid,
            "kty": self.kty,
            "use": self.use,
            "alg": self.alg,
            "x5t": self.getSHA1Thumbprint(),
            "x5t#S256": self.getSHA256Thumbprint(),
        }

    @classmethod
    def newKey(use: UseTypes, size: int):
        pass

class RSASize(int, Enum):
    small = 256
    mid = 384
    long = 512

class RSAKey(Key):
    def __init__(self, key: jwk.JWK, kid: str, use: UseTypes, size: RSASize):
        alg = AlgTypes.RS256
        if size == 384:
            alg = AlgTypes.RS384
        elif size == 512:
            alg = AlgTypes.RS512
        super().__init__(key, kid, KeyType.RSA, use, alg)
        self.size = size

    @classmethod
    def newKey(cls, use: UseTypes, size: RSASize):
        key = jwk.JWK.generate(kty='RSA', size=2048)
        key.kid = key.thumbprint()
        return cls(key, key.thumbprint(), use, RSASize)

class KeyStore():
    def __init__(self, use: UseTypes, activeTime: timedelta, retireTime = timedelta):
        """

        Args:
            activeTime (timedelta): Time of key being active
            retireTime (timedelta, optional): Time of key being retired
        """
        self.activeKeys: Dict[str, Key] = {}
        self.retiredKeys: Dict[str, Key] = {}
        self.activeTime = activeTime
        self.retireTime = retireTime
        self.use = use
        self.keyset = jwk.JWKSet()


    def addKey(self, key: Key):
        if(key.kid in self.activeKeys or key.kid in self.retiredKeys):
            return False
        else:
            key.activationTime = datetime.now()
            self.activeKeys[key.kid] = key
            self.keyset.add(key.key)
            return True

    def retireKey(self, keyId: str):
        if(keyId not in self.activeKeys):
            return False
        else:
            self.retiredKeys[keyId] = self.activeKeys[keyId]
            del self.activeKeys[keyId]
            return True

    def removeKey(self, keyId: str):
        if(keyId not in self.retiredKeys):
            return False
        else:
            del self.retiredKeys[keyId]
            keysToKeep = [k for k in self.keyset["keys"] if k.get("kid") != keyId]
            self.keyset = jwk.JWKSet()
            for k in keysToKeep:
                self.keyset.add(jwk.JWK(**k))
            return True

    def getActiveKey(self, keyId):
        if(keyId not in self.activeKeys):
            return None
        else:
            return self.activeKeys[keyId]

    def getFirstActiveKey(self):
        if len(self.activeKeys) == 0:
            return None
        else:
            return self.activeKeys[next(iter(self.activeKeys))]

    def getActiveOrRetiredKey(self, keyId):
        if(keyId not in self.activeKeys):
            if(keyId not in self.retiredKeys):
                return None
            else:
                return self.retiredKeys[keyId]
        else:
            return self.activeKeys[keyId]

    def getKeyset(self):
        return self.keyset

    def keysInfo(self):
        keys = []
        for keyId in self.activeKeys:
            keys.append(self.activeKeys[keyId].publicInfo())
        return keys

    def update(self):
        for keyId in list(self.activeKeys):
            key = self.activeKeys[keyId]
            if key.activationTime + self.activeTime < datetime.now():
                self.retireKey(key.kid)
        for keyId in list(self.retiredKeys):
            key = self.retiredKeys[keyId]
            if key.activationTime + self.activeTime + self.retireTime < datetime.now():
                self.removeKey(key.kid)
        if len(self.activeKeys) == 0:
            self.addKey(RSAKey.newKey(self.use, RSASize.long))
