from datetime import datetime, timedelta


def datetime_diff(a, b):
    return (a - b).total_seconds()

a = datetime.now()
b = datetime.now() - timedelta(days=5)
print(datetime_diff(a, b))
