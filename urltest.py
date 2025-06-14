# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
position =3
count =4
# url = input('Enter - ')
url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('a')
def get_link_at_position(url, position):
    if 1<= position <=len(tags):
        tag = tags[position - 1]
        next_url = tag.get('href', None)
        link_text = tag.contents[0] if tag.contents else ''  # Get the text within the tag
        return next_url, link_text
        # print(next_url, link_text)
for i in range(count):
    nexturl,name = get_link_at_position(url,position)
    print(f"Following link to: {nexturl}")
    print(f"Name found: {name}")
# while count < 4:
#     print(count)
#     count = count + 1
#     tags = soup('a')

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
    # print(tag.get('href', None))