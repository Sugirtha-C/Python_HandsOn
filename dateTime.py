
from datetime import datetime,date
import time
import pytz #install this from pycharm>Settings>select your project> Interpreter

now=datetime.now()
print(now)

current_time=now.time()
print(current_time)

current_date=now.date()
print(current_date)

print("year:", now.year)
print("second:", now.second)
print("microsecond:", now.microsecond)

today=date.today()
print(today)

t=time.time()
print(t)

print(time.ctime(time.time()))


dt_us_central=datetime.now(pytz.timezone('US/Central'))
print(dt_us_central)

dt_iso=datetime.now().isoformat()
print("ISO Format:",dt_iso)