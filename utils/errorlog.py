import logging
import time

def weberrorlog(message = "", code = 200):
    logging.warning(message)
    return {"state": 1, "time":time.time()}, code