from datetime import datetime, date, time
from .errorListFile import errorList

def datetimeFromString(date: str):
    """Attempts to parse datetime from string

    Args:
        date (str): string that datetime is in

    Raises:
        errorList.data.couldNotConvertDate: unable to convert

    Returns:
        datetime.date: exported datetime
    """
    try:
        return datetime.fromisoformat(date)
    except ValueError as e:
        raise errorList.data.couldNotConvertDate

def dateFromString(date: str):
    """Attempts to parse date from string

    Args:
        date (str): string that date is in

    Raises:
        errorList.data.couldNotConvertDate: unable to convert

    Returns:
        datetime.date: exported date
    """
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        raise errorList.data.couldNotConvertDate

def timeFromString(time: str):
    """Attempts to parse time from string

    Args:
        time (str): string that time is in

    Raises:
        errorList.data.couldNotConvertDate: unable to convert

    Returns:
        datetime.time: exported time
    """
    try:
        return datetime.strptime(time, "%H:%M:%S").time()
    except ValueError as e:
        raise errorList.data.couldNotConvertDate
