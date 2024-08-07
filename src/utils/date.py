from datetime import datetime, date, time
from utils.errorList import errorList

def dateFromString(date: str):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        raise errorList.data.couldNotConvertDate

def timeFromString(time: str):
    try:
        return datetime.strptime(time, "%H:%M:%S").time()
    except ValueError as e:
        raise errorList.data.couldNotConvertDate
