import json
import urllib.request
url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = json.loads(data)
# print(tree)
comments = tree['comments']
sum =0
count =0
for comment in comments:
    count = count + 1
    sum = sum + int(comment['count'])
print('Count:', count)
print('Sum:', sum)