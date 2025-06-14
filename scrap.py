# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urltest.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
# url='http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count =0;
sum =0;
for tag in tags:
    print(tag)
    # count = count+1
    value = int(tag.contents[0])
    # Look at the parts of a tag
    print(value)
#     for value in tag.contents[0]:
    sum = sum + int(value)
    count = count +1
#
#     #print('TAG:', tag.get('comments',None))
#     # print('URL:', tag.get('href', None))
#     # print('Contents:', tag.contents[0])
#     # print('Attrs:', tag.attrs)
print('Count',count)
print('Sum',sum)