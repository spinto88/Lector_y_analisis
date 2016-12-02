#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa guarda las notas de la página de Clarín
de las 18:00 hs
"""

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup as BS
import codecs
import datetime as dt
import os

# Directorio donde se guarda.
today = dt.date.today()

directory = os.getcwd() + '/Clarin_portada_' + str(today)
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
    os.remove('Resumen' + today + '.txt')
except:
    pass
fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo, Seccion' + '\n')
fp.close()

if True:

    # LLamado a la pagina
    pagina = 'http://www.clarin.com/'
    html = urlopen(pagina).read()
    soup = BS(html, 'html.parser')
    articles = soup.findAll('article')

    for article in articles: 
        data_article = article.find('a')
        if data_article != None:
            try:
                link = pagina + data_article['href']
                html = urlopen(link).read() 

    	        # Lectura de la nota como html y extracción del contenido.
                soup = BS(html, 'html.parser')

                title = soup.find(property = 'og:title')['content']
                try:
                    description = soup.find(name = 'DESCRIPTION')['content']
                except:
                    description = ''

                try:
                    content = soup.find(property = 'og:description')['content']
                except:
                    content = ''
 
                try: 
                    section = soup.find(property = 'og:section')['content']
                except:
                    section = ''
 
            # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
                fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
                fp.write(str(today) + '\n' + section + '\n' + title + '\n' + description + '\n' + content + '\n')
                fp.close()

                # Guardado del titulo e id para rápida identificación.
                fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
                fp.write(str(id_nota) + '\t' + title + '\t' + section + '\n')
                fp.close()

                id_nota += 1

            except:
                continue
            
            
