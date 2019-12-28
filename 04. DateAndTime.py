import datetime as dt
import time as tm

print(tm.time)

dtnow = dt.datetime.fromtimestamp(tm.time())

print(dtnow)

print(dtnow.year)
print(dtnow.month)
print(dtnow.day)
print(dtnow.hour)
print(dtnow.minute)
print(dtnow.second)
print(dtnow.microsecond)

delta = dt.timedelta(days = 100)
print(delta)

today = dt.datetime.today()
print(today)

print(today - delta)

print(today > (today - delta))
