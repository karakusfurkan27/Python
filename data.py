from datetime import datetime
from datetime import date
#from datetime import time

import datetime

result = dir(datetime.datetime)
# result = dir(datetime.time)
# result = dir(datetime.date)

simdi = date.now()

#result = date.now()
result = simdi.year
result = simdi.month
result = simdi.day
print(result)