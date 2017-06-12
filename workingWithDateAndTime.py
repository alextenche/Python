import datetime

# print(dir(datetime))

now = datetime.datetime.now()
start_work = now.replace(hour=12, minute=12)

time_worked = now - start_work
print(time_worked)
print(time_worked.days)
print(time_worked.seconds)
print(time_worked.microseconds)

hours_worked = round(time_worked.seconds / 3600)
print(hours_worked)

datetime.timedelta(days=5)
print(now + datetime.timedelta(days=5))

print(now.date)

print(now.time)


def far_away(time_interval):
    return datetime.datetime.now() + time_interval


today = datetime.datetime.today()
print(today)
today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today)

print(today.weekday())

print(now.timestamp())


def minutes(dt1, dt2):
    return round((dt1 - dt2).total_seconds() / 60)


print(minutes(now, start_work))
