# %%
import datetime
import os

filename = "/Users/saurabhkumarsingh/Documents/GitHub/Dataset/testfile.txt"

#file = open(filename)

os.path.getsize(filename)
timestamp = os.path.getmtime(filename)

# %%
# %%
datetime.datetime.fromtimestamp(timestamp)
# %%
os.path.abspath(filename)

# %%
