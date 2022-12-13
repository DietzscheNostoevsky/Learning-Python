# improved focusing time based on Huberman videos
#
# Not Pomodoro
# Focus for 90 minutes Ultradian rhythm
# 90 minute implementd using Pomodoro Timer
#
# Implementing random microrests using Python

# Todo

# Microrests are 10 secs breaks to be implemented randomly after starting this programme
# A timer will ring from the time between 5-20 mins random.
# Min 5 mins
# Max 15 mins between breaks

# ------------------------------------------------------------
#!/usr/bin/env python3

# importing libraries
import os
import random
import time


def microrests():
    """outputs a sound to take a break for 10 seconds and then resume work
    """
    os.system("say break")
    time.sleep(10)
    os.system("say resume")


microrests()
