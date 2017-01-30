import dryscrape
from bs4 import BeautifulSoup as BS

sess = dryscrape.Session(base_url = 'http://buscar.lanacion.com.ar')
sess2 = dryscrape.Session()

# we don't need images
sess.set_attribute('auto_load_images', False)
sess2.set_attribute('auto_load_images', False)


for i in range(1, 2):
    sess.visit('/Mauricio Macri/page-' + str(i))
    for link in sess.xpath('//h2/a[@href]'):
        try:
            sess2.visit(link['href'])
            body = sess2.body()
            soup = BS(body)
            print soup.find('h1',{'itemprop':'headline'}).getText()
        except:
            pass
        
