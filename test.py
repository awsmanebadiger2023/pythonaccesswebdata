import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

starting_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_link_at_position(url, position):
        print('Retrieving:', current_url)
        # Open the URL with SSL context
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('a')
        # print(tags)
        tag = tags[position-1]
        next_url = tag.get('href', None)
        link_text = tag.contents[0]# if 1 <= position <= len(tags):

        return next_url, link_text

# --- Main Program Logic ---

last_name = None
sequence_of_names = []
current_url = input('Enter URL:')
# current_url = current_name
count = input('Enter count:')
counter = int(count)+1
position = input('Enter position:')
# print('Retrieving:', current_url)

for i in range(int(counter)):

    next_url, name = get_link_at_position(current_url, int(position))
    current_url = next_url
