from datetime import date,  timedelta, datetime

today = date.today()
tomorrow = date.today() + timedelta(1)
yesterday = date.today() - timedelta(1)

print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)