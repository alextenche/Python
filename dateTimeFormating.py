import datetime

now = datetime.datetime.now()

print(now.strftime('%B %d'))
print(now.strftime('%m/%d/%Y'))

birthday = datetime.datetime.strptime('24-07-1978', '%d-%m-%Y')
print(birthday)


def to_string(date_string):
    return date_string.strftime('%d %B %Y')


def from_string(dt_string, dt_format):
    return datetime.datetime.strptime(dt_string, dt_format)


test = from_string("09/24/12 18:30", "%m/%d/%y %H:%M")
print(test)
