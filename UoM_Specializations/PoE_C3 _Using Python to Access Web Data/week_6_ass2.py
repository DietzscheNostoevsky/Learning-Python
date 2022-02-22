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

loc = input('Enter Location - ')

baseurl = 'http://py4e-data.dr-chuck.net/json?'
params = {}
params['address'] = loc
params['key'] = 42
url = baseurl + urllib.parse.urlencode(params)


print(f"Retreiving : {url}")

uh = urllib.request.urlopen(url, context=ctx).read()

data = json.loads(uh)

place_id = data['results'][0]['place_id']
print(place_id)
