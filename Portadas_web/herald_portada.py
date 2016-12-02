#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa guarda las notas de la página 
del Buenos Aires Herald de las 18:00 hs.
"""

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup as BS
import codecs
import datetime as dt
import os

# Directorio donde se guarda.
today = dt.date.today()

directory = os.getcwd() + '/Herald_portada_' + str(today)
try:
    os.remove(directory)
except:
    pass
try:
    os.mkdir(directory)
except:
    pass
os.chdir(directory)

id_nota = 0

# Guardado del titulo e id para rápida identificación.

try:
    os.remove('Resumen' + str(today) + '.txt')
except:
    pass
fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo' + '\n')
fp.close()

if True:

    # LLamado a la pagina
    pagina = 'http://buenosairesherald.com/'
    html = urlopen(pagina).read()
    soup = BS(html, 'html.parser')
    articles = soup.findAll('div', {'class':'nota'})

    for article in articles: 
        data_article = article.find('a')
        if data_article != None:
            try:
                title = data_article.getText()
                link = pagina + data_article['href']
                html = urlopen(link).read() 

    	        # Lectura de la nota como html y extracción del contenido.
                soup = BS(html, 'html.parser')

                content = soup.find('div', {'style':'float:none'}).getText()
 
                # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
                fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
                fp.write(str(today) + '\n' + title + '\n' + content + '\n')
                fp.close()

                # Guardado del titulo e id para rápida identificación.
                fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
                fp.write(str(id_nota) + '\t' + title + '\n')
                fp.close()

                id_nota += 1

            except:
                continue
