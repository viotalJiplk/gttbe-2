from datetime import timedelta, time

def fromTimeDelta(td: timedelta):
    totalSeconds = td.total_seconds()
    hours = int(totalSeconds // 3600)
    minutes = int((totalSeconds % 3600) // 60)
    seconds = int(totalSeconds % 60)
    return time(hour=hours, minute=minutes, second=seconds)
