import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

url = 'http://www.pythonchallenge.com/pc/def/0.html'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html5lib')
img = soup.find('img')['src']
img_url = 'http://www.pythonchallenge.com/pc/def/' + img
print(img_url)
urlretrieve(img_url, '0.jpg')
# print(img)

url_next = 'http://www.pythonchallenge.com/pc/def/%d.html' % 2 ** 38
print(url_next)
r = requests.get(url_next)
print(r.text)

