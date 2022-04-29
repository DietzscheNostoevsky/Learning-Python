#!/usr/bin/env python

# To calculate how much data to remain at the end of the day
# and how much data I can use per day

# %%
import datetime

end_date = datetime.date(2022, 5, 20)

end = end_date.strftime("%d-%m-%Y")

today = datetime.date.today()
# %%

#data_today = input("Enter data remaining (GB) :  ")
data_today = 38
days_remain = end_date - today
data_to_remain = 2
util_data = data_today - data_to_remain

# %%
per_day_usage = util_data / days_remain.days
print(per_day_usage, "GB")
# %%
