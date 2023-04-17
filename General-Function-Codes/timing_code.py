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


# Get the current time in UTC timezone
now_utc = datetime.datetime.utcnow()

# Create a timezone object for Indian Standard Time (IST)
ist_tz = pytz.timezone('Asia/Kolkata')

# Convert the current time from UTC to IST
now_ist = now_utc.astimezone(ist_tz)

# Print the current time in IST timezone
print("Current time in IST:", now_ist.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
