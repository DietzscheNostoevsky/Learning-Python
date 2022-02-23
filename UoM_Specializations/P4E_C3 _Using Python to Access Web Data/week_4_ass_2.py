# Following Links in Python

# In this assignment you will write a Python program
# that expands on http: // www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
# extract the href = vaues from the anchor tags,
# scan for a tag that is in a particular position
# relative to the first name in the list,
# follow that link and repeat the process a number
# of times and report the last name you find.

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# $ python3 solution.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html


# %%
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import os

os.system("clear")

# %%
# -----------------------------------------

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# %%
# -----------------------------------------

# Get the user input
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = input('Enter URL - ')
count = int(input('Enter Count :'))
position = int(input('Enter Position : '))


# %%

for i in range(count):
    print(f"Retreiving : {url}")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    nametags = soup('a')
    required_nametag = nametags[position-1]
    required_url = required_nametag.get('href')
    name_on_url = required_nametag.contents
    url = required_url
print('Required Name :', name_on_url[0])

# %%
