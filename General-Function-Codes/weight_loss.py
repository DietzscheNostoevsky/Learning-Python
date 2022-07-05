#!/usr/bin/env python

# First create a DB for weight tracking
# %%
import datetime
from datetime import timedelta

end_date = datetime.date(2022, 6, 5)

end = end_date.strftime("%d-%m-%Y")

today = datetime.date.today()

# %%
present_weight = int(input("Insert present weight in KG : "))
target_delta = int(input("Insert target loss per week : ") or "1")
goal_weight = int(input("Insert Goal Weight : ") or "77")
