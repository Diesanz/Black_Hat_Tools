from io import BytesIO
from lxml import etree

import requests

url = 'https://nostarch.com'

r = requests.get(url)
content = r.content # is of type 'bytes'

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser) #parse into tree

for link in content.findall('//a'): 
	print(f"{link.get('href')} -> {link.text}")
