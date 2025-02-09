from datetime import date,  timedelta, datetime

a = datetime.now()
b = a.strftime("%Y-%m-%d, %H:%M:%S")
print(b)