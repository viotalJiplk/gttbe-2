import logging
import time

def weberrorlog(message = "", code = 200, kind = ""):
    logging.warning(({"kind": kind, "msg": message,"time":time.time()}, code))
    return {"kind": kind, "msg": message,"time":time.time()}, code