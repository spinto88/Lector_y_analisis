from urllib2 import urlopen
import datetime as dt
from bs4 import BeautifulSoup as BS
import os 
import Image


pagina = 'http://www.diarios-argentinos.com/'
html = urlopen(pagina).read()
soup = BS(html, 'html.parser')

items = soup.findAll('div', {'class':'item'})

id_tapa = 0
for item in items:
    try:
        link = pagina + item.find('img')['src']
    except:
        continue

    img = urlopen(link)

    image = Image.open(img.read())

    image.thumbnails((800,800)) # Changing the size
    image.save(str(id_tapa) + '.jpg', 'wb')

    id_tapa += 1
