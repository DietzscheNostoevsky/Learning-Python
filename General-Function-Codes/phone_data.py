#!/usr/bin/env python

# To calculate how much data to remain at the end of the day
# and how much data I can use per day

# %%
import datetime
from datetime import timedelta

end_date = datetime.date(2022, 6, 22)

end = end_date.strftime("%d-%m-%Y")

today = datetime.date.today()
# %%

data_today = input("Enter data remaining (GB) :  ")
data_today = float(data_today)
#data_today = 38
days_remain = end_date - today
data_to_remain = 0
util_data = data_today - data_to_remain

# %%
per_day_usage = util_data / days_remain.days
per_day_usage = round(per_day_usage, 2)
print("-------------------------------------------", "\n")
print("Today = ", data_today, "GB")
print("Per day usage = ", per_day_usage, "GB", "\n")
print("-------------------------------------------", "\n")

# %%

print("Closing Data Per Day ", "\n")
for i in range(days_remain.days):
    print(today, ':', util_data, "GB")
    util_data = util_data - per_day_usage
    util_data = round(util_data, 2)
    today = today + timedelta(1)

print("\n")
print("********************************************", "\n")

# %%
