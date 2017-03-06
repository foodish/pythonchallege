import requests
import re
from urllib.request import urlretrieve


# a = [chr(i) for i in range(97,123)]
# print(chr(ord('z') + 1))

url_1 = 'http://www.pythonchallenge.com/pc/def/map.html'
r = requests.get(url_1).text
print(r)
img_name = re.findall('src="(.*?)"', r)[0]
text = re.findall(r'color="#f000f0">(.*?)</tr>', r, re.S)[0].strip()
img_url = 'http://www.pythonchallenge.com/pc/def/' + img_name
urlretrieve(img_url, '1.jpg')

text_1 = text.split(' ')
for word in text_1:
    w = ''
    for char in word:
        if char.isalpha() and char not in 'yz' :
            w += chr(ord(char)+2)
        if char == 'y':
            w += 'a'
        if char == 'z':
            w += 'b'
        
    print(w)
    w = ''


# print(r,img_name, img_url)
