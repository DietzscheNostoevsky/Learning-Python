# Extracting Data from XML
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import xml.etree.ElementTree as ET

from sympy import re


os.system("clear")

# -----------------------------------------

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# -----------------------------------------

url = input('Enter URL - ')
#url = "http://py4e-data.dr-chuck.net/comments_42.xml"
print(f"Retreiving : {url}")

uh = urllib.request.urlopen(url, context=ctx).read()
data = uh

print('Retrieved', len(data), 'characters')
# print(data.decode())

tree = ET.fromstring(data)
results = tree.findall('comments/comment')

count = 0
sum = 0
for i in results:
    a = int(i.find('count').text)
    sum += a
    count += 1
print(f"Count = {count}")
print(f"Sum = {sum}")
