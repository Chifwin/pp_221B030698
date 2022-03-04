from datetime import datetime, timedelta


def drop_microsec(a:datetime):
    return a - timedelta(microseconds=a.microsecond)

print(drop_microsec(datetime.now()))