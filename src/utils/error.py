from functools import wraps

def handleReturnableError(func):
    @wraps(func)
    def wrapReturnableError(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ReturnableError as e:
            return {"kind": e.kind, "msg": str(e)}, e.httpStatusCode
    return wrapReturnableError

class ReturnableError(Exception):
    def __init__(self, message: str, kind: str, httpStatusCode: int = 500):
        super().__init__(message)
        self.message = message
        self.httpStatusCode = httpStatusCode
        self.kind = kind
