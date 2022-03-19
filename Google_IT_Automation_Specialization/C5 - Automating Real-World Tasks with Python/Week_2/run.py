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


# %%
