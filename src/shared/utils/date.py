from datetime import timedelta, time

def fromTimeDelta(td: timedelta):
    """Calculates time from timedelta

    Args:
        td (timedelta): timedelta to calculate from

    Returns:
        time: time calculated
    """
    totalSeconds = td.total_seconds()
    hours = int(totalSeconds // 3600)
    minutes = int((totalSeconds % 3600) // 60)
    seconds = int(totalSeconds % 60)
    return time(hour=hours, minute=minutes, second=seconds)
