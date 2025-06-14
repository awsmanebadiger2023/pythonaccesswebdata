import re
import urllib.request
url = 'http://py4e-data.dr-chuck.net/regex_sum_2239693.txt'
uh = urllib.request.urlopen(url)
data = uh.read()
# print(data)
# print(data.decode())
numList = re.findall('[0-9]+', data.decode())
# print(numList)
sum=0;
for num in numList:
    sum = sum + int(num)

print(sum)