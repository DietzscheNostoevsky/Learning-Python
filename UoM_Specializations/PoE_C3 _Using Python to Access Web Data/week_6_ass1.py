# Extracting Data from JSON

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import xml.etree.ElementTree as ET

from sympy import re
import json


os.system("clear")

# -----------------------------------------

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# -----------------------------------------

#url = input('Enter URL - ')
url = "http://py4e-data.dr-chuck.net/comments_42.json"
print(f"Retreiving : {url}")

uh = urllib.request.urlopen(url, context=ctx).read()

data = json.loads(uh)
comments = data['comments']
sum = 0
count = 0

for i in comments:
    num = int(i['count'])
    sum += num
    count += 1

print(f"Count = {count}")
print(f"Sum = {sum}")
