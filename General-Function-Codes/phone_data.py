#!/usr/bin/env python

# To calculate how much data to remain at the end of the day
# and how much data I can use per day

# %%
import datetime

end_date = datetime.date(2022, 5, 20)

end = end_date.strftime("%d-%m-%Y")

today = datetime.date.today()
# %%

data_today = input("Enter data remaining : ")
