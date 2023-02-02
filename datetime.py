import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
print(now.year)
#to find a date in the future use timedelta
print(now + datetime.timedelta(days=19))
