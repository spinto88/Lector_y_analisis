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
import json
import os

# Directorio donde se guarda.
today = dt.date.today()

directory = os.getcwd() + '/LaNacion_impresa_' + str(today)
try:
    os.mkdir(directory)
except:
    pass
os.chdir(directory)

id_nota = 0

# Guardado del titulo e id para rápida identificación.
fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo, Seccion' + '\n')
fp.close()

if True:

    # LLamado al RSS.
    pagina = 'http://contenidos.lanacion.com.ar/herramientas/rss-origen=1'
    feed = feedparser.parse(pagina)

    # Recorrido sobre las notas de la sección.
    for nota in feed['items']:

        # Título, subtitulo, fecha.
        title = nota['title']
        updated = nota['updated']
        date, time = updated.split('T')
        date = date.split('-') 
        date = dt.date(int(date[0]), int(date[1]), int(date[2]))
        
        if True:

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

            # Para la sección
            try:
                json_string = json.loads(data_section)
                section = json_string['articleSection']
            except:
                data_section = ''
                data_section_aux = soup.findAll('script')
                for data in data_section_aux:
                    data_section += data.getText()
                data_section = data_section.split(';')
                for text in data_section:
                    if 'LN.NotaDM.section' in text:
                        text = text.split('=')
                        text[1] = text[1].replace('"','')
                        text[1] = text[1].replace(' ','')
                        section = text[1]
                        break
            
            # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
                       
            fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
            fp.write(str(date) + '\n' + section + '\n' + title + '\n' + description + '\n' + content + '\n')
            fp.close()

            # Guardado del titulo e id para rápida identificación.
            fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
            fp.write(str(id_nota) + '\t' + title + '\t' + section + '\n')
            fp.close()

            id_nota += 1 
