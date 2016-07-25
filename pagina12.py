#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa guarda las últimas noticias del RSS del diario Página 12,
tomadas a las 18:00 hs.
"""

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup as BS
import codecs
import datetime as dt
import os

# Directorio donde se guarda.
today = dt.date.today()

directory = os.getcwd() + '/Pagina12_' + str(today)
try:
    os.mkdir(directory)
except:
    pass
os.chdir(directory)

# Secciones a tener en cuenta.
secciones = ['Ultimas_noticias']

id_nota = 0

# Guardado del titulo e id para rápida identificación.

fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo' + '\n')
fp.close()


for seccion in secciones:

    # LLamado al RSS.
    pagina = 'http://www.pagina12.com.ar/diario/rss/' + seccion.lower() + '.xml'
    feed = feedparser.parse(pagina)

    # Recorrido sobre las notas de la sección.
    for i in range(len(feed['entries'])):

        # Nota como RSS.
        nota = feed['entries'][i]

        
        # Título, subtitulo, fecha.
        title = nota['title']
        description = nota['description']
        date = nota['published_parsed']
        date = dt.date(date.tm_year, date.tm_mon, date.tm_mday)
        
        # Guarda la nota si es del día de hoy o del día de ayer.
        day_offset = dt.timedelta(days = 1)
        if date >= (today - day_offset):

            soup = BS(description, 'html.parser')
            text = soup.get_text().replace('\n', '')

            # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
            fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
            fp.write(str(date) + '\n' + title + '\n' + text + '\n')
            fp.close()

            # Guardado del titulo e id para rápida identificación.
            fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
            fp.write(str(id_nota) + '\t' + title + '\n')
            fp.close()

            id_nota += 1 
