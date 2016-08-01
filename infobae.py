#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa guarda las notas del RSS del diario Infobae.
Dentro de la carpeta con un dado día, guarda las notas que aparecieron
ese mismo día antes de las 18:00hs mas las notas del día anterior.
"""

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup as BS
import codecs
import datetime as dt
import os

# Directorio donde se guarda.
today = dt.date.today()

directory = os.getcwd() + '/Infobae_' + str(today)
try:
    os.mkdir(directory)
except:
    pass
os.chdir(directory)


# Secciones a tener en cuenta.
secciones = ['Politica', 'Mundo', 'Sociedad', 'Policiales', 'Ciudades', 'Opinion', 'Cultura', 'Deportes']

id_nota = 0

# Guardado del titulo e id para rápida identificación.
fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo, Seccion' + '\n')
fp.close()

id_nota = 0
for seccion in ['']:

    # LLamado al RSS.
    pagina = 'http://www.infobae.com/argentina-rss.xml'
    feed = feedparser.parse(pagina)

    # Recorrido sobre las notas de la sección.
    for i in range(len(feed['items'])):

        # Nota como RSS.
        nota = feed['items'][i]

        # Título, subtitulo, fecha.
        title = nota['title']
        description = nota['description']
        date = nota['published_parsed']
        date = dt.date(date.tm_year, date.tm_mon, date.tm_mday)
        
        # Guarda la nota si es del día de hoy o del día de ayer.
        day_offset = dt.timedelta(days = 1)
        if date >= (today - day_offset):

            # Link de la nota.
            link = nota['link']

	    # Lectura de la nota como html y extracción del contenido.
            html = urlopen(link).read() 
            soup = BS(html, 'html.parser')
            contents = soup.find_all('p', 'element element-paragraph')
            content = ''
            for data in contents:
                content += data.getText()
            
            # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
            fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
            fp.write(str(date) + '\n' + seccion + '\n' + title + '\n' + description + '\n' + content + '\n')
            fp.close()
            
            # Guardado del titulo e id para rápida identificación.
            fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
            fp.write(str(id_nota) + '\t' + title + '\t' + seccion + '\n')
            fp.close()
            
            id_nota += 1
