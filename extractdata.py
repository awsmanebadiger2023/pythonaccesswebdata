import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
# print(data)
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
# sum=0;
counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    # print(result.text)
    nums.append(int(result.text))
# print(nums)
total = sum(nums)
print('Count:', len(nums))
print('Sum:', total)