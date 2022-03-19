#!/usr/bin/env python3

# %%
import os
import requests

dir = 'data/feedback'

files = os.listdir(dir)

# %%
for file in files:
    filepath = os.path.join(dir, file)
    with open(filepath, 'r') as text:
        lines = text.readlines()
        postdict = dict()
        postdict['title'] = lines[0].strip()
        postdict['name'] = lines[1].strip()
        postdict['date'] = lines[2].strip()
        postdict['feedback'] = lines[3].strip()


# %%
