#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

# using example source code


def upload(file, url):
    with open(file, "rb") as opened:
        requests.post(url, files={"file": opened})


image_dir = "supplier-data/images/"

# creating a list of all dirs of images to upload
image_files = [
    image_dir + file for file in os.listdir(image_dir) if file.endswith(".jpeg")]

for file in image_files:
    upload(file, url)
