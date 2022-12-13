# improved focusing time based on Huberman videos
#
# Not Pomodoro
# Focus for 90 minutes Ultradian rhythm
# 90 minute implementd using Pomodoro Timer
#
# Implementing random microrests using Python

# Todo

# Microrests are 10 secs breaks to be implemented randomly after starting this programme
# reference https://www.youtube.com/watch?v=EhXLPdhtAHc
# A timer will ring from the time between 5-15 mins random.
# Min 5 mins
# Max 15 mins between breaks

# ------------------------------------------------------------
#!/usr/bin/env python3

# importing libraries
from datetime import datetime
import os
import random
import time
from datetime import date


def microrests():
    """outputs a sound to take a break for 10 seconds and then resume work
    """
    print("take a 10 sec break")
    os.system("say break")
    time.sleep(10)
    print("Resume")
    os.system("say resume")


# %%
TODAY = date.today()
d1 = TODAY.strftime("%d/%m/%Y")  # start date with dd-mm-yy format
NOW = datetime.now()
current_time = NOW.strftime("%H:%M:%S")
print("Today : ", d1)
print("Start Time :", current_time)


# %%

def worksets():
    """Work in 15 minute sets. 
    A microrest in called at random time bewteen the time duration
    But only after 7 minutes in a set 

    """
    from datetime import datetime
    NOW = datetime.now()
    current_time = NOW.strftime("%H:%M:%S")
    print("Set start")
    print("Start Time :", current_time)
    import random
    ran = random.randrange(7, 15)
    for i in range(15):
        print(i+1, ":", datetime.now().strftime("%H:%M:%S"))
        if i == ran:
            microrests()
        time.sleep(60)
    print("------- 15 Min set COMPLETE -------")
# %%


for i in range(1, 7):
    print("Set : ", i)
    os.system("say set start")
    worksets()

os.system("say Focus Time Over")
