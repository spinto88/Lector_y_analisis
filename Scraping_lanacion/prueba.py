import dryscrape
from bs4 import BeautifulSoup as BS
import codecs

session = dryscrape.Session(base_url = 'http://buscar.lanacion.com.ar')
session.set_attribute('auto_load_images', value = False)

fp = codecs.open('Titulos_comentarios.txt','a','utf8')
#fp.write('#Titulo\tCantidad de comentarios\tFecha\n')

for page in range(90,100):

    session.visit('/macri/page-' + str(page))

    session2 = dryscrape.Session()
    session2.set_attribute('auto_load_images', value = False)

    links = session.xpath('//h2/a[@href]')[1:]
    links = [link['href'] for link in links]

    session.reset()
    for link in links:
        session2.visit(link)
        body = session2.body()
        soup = BS(body)
        try:
            title = soup.find('h1', {'itemprop': 'headline'}).getText()
            comments = str(int(soup.find('span', {'class':'total lf'}).getText()))
            date = str(soup.find('meta',{'itemprop':'datePublished'}).get('content'))
            fp.write(title + '\t' + comments + '\t' + date + '\n')
        except:
            pass

    print 'Page completed: ' + str(page)

fp.close()
