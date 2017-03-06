import requests
from urllib.request import urlretrieve
import re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
img_url = 'http://www.pythonchallenge.com/pc/def/ocr.jpg'
r = requests.get(url).text
#urlretrieve(img_url, '2.jpg')
text = re.findall('<!--(.*?)-->', r, re.S)[-1].strip()
#print(text)

tmp = set()
tm = []

for i in text:
    tmp.add(i)
    tm.append(i)
    
for i in tmp:
    print(i, text.count(i))
    
