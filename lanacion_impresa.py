#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa guarda las notas del RSS del diario LaNacion, 
pertenecientes a la edición impresa.
"""

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup as BS
import codecs
import datetime as dt
import os

# Directorio donde se guarda.
today = dt.date.today()

directory = os.getcwd() + '/LaNacion_impresa_' + str(today)
try:
    os.mkdir(directory)
except:
    pass
os.chdir(directory)

# Secciones a tener en cuenta.
secciones = ['Politica', 'Economia', 'Deportes', 'Sociedad', 'Seguridad', 'Buenos Aires', 'Opinion', 'Espectaculos', 'El Mundo']
id_secciones = ['30', '272', '131', '7773', '7775', '7774', '28', '120', '7']

id_nota = 0
"""
# Guardado del titulo e id para rápida identificación.
fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo, Seccion' + '\n')
fp.close()
"""
for seccion in secciones:

    # LLamado al RSS.
    pagina = 'http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=' + id_secciones[secciones.index(seccion)]
    feed = feedparser.parse(pagina)
    
    pagina_titulos = 'http://contenidos.lanacion.com.ar/herramientas/rss-origen=1'
    fp = codecs.open('Titulos.txt', 'a', 'utf8')
    feed_titulos = feedparser.parse(pagina_titulos)
    for items in feed_titulos['items']:
        fp.write(items['title'] + '\n')
    fp.close()
    #print len(feed_titulos['items'])
#    break
    """

    # Recorrido sobre las notas de la sección.
    for i in range(len(feed['items'])):

        # Nota como RSS.
        nota = feed['items'][i]

        # Título, subtitulo, fecha.
        title = nota['title']
        updated = nota['updated']
        date, time = updated.split('T')
        date = date.split('-') 
        date = dt.date(int(date[0]), int(date[1]), int(date[2]))
        
        if date == today and time == '00:00:00-03:00':

            # Link de la nota.
            link = nota['link']

	    # Lectura de la nota como html y extracción del contenido.
            html = urlopen(link).read() 
            soup = BS(html, 'html.parser')

            try:
                description = soup.find(itemprop = 'description').getText()
            except:
                description = ''
            try:
                content_first = soup.find('p', {'class': 'primero'}).getText()
            except:
                content_first = ''

            contents_body = soup.find_all('p', {'class': ''})
            content = content_first
            for tag in contents_body:
                try:
                    content += tag.getText()
                except: 
                    pass
            
            # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
            fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
            fp.write(str(date) + '\n' + seccion + '\n' + title + '\n' + description + '\n' + content + '\n')
            fp.close()

            # Guardado del titulo e id para rápida identificación.
            fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
            fp.write(str(id_nota) + '\t' + title + '\t' + seccion + '\n')
            fp.close()

            id_nota += 1

    """
