from datetime import datetime, timedelta

date = datetime.now()

print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
print(date.weekday())
print(date.isoweekday())
print(date.isoformat())
print(date.timetuple())

date = datetime(2020, 1, 1)
print(date)

date = datetime.strptime('2020-01-01', '%Y-%m-%d')
print(date)

date = datetime.fromisoformat('2020-01-01')
print(date)

date = datetime.fromtimestamp(1577836800)
print(date)

# timedelta
dt1 = datetime(2020, 1, 1)
dt2 = datetime(2020, 2, 1)
delta = dt2 - dt1

print(delta)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())

dt3 = dt1 + timedelta(days=1)
print(dt3)
