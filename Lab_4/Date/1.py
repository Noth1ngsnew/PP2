from datetime import date,  timedelta, datetime

current = date.today()
Five_days_ago = date.today() - timedelta(5)

print("The current day: ", current)
print("Five days ago: ", Five_days_ago)