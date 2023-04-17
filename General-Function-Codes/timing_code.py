import pytz
import time
import datetime

t0 = time.time()
now = datetime.datetime.now()
print("Current time:", now)

time.sleep(5)

print("Took:{0:.2f}s".format(time.time() - t0))
now = datetime.datetime.now()
print("Current time:", now)
