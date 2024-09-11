from functools import wraps
from flask_restx import fields
def handleReturnableError(func):
    """Decorator to handle returnableErrors"""
    @wraps(func)
    def wrapReturnableError(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ReturnableError as e:
            return e.returnDict(), e.httpStatusCode
    return wrapReturnableError

class ReturnableError(Exception):
    """Error that can be handled and returned to user"""
    def __init__(self, message: str, kind: str, httpStatusCode: int = 500):
        """Initializes error that can be handled and returned to user

        Args:
            message (str): message to return to user
            kind (str): kind of error
            httpStatusCode (int, optional): http status code  Defaults to 500.
        """
        super().__init__(message)
        self.message = message
        self.httpStatusCode = httpStatusCode
        self.kind = kind

    def returnDict(self):
        return {"kind": self.kind, "msg": self.message}
    def returnModel(self):
        return {"kind": fields.String, "msg": fields.String}
