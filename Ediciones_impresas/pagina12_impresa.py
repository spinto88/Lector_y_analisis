#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este programa guarda las noticias de la edición
impresa del diario Página 12.
"""
import feedparser
from urllib2 import Request
from urllib2 import urlopen
from bs4 import BeautifulSoup as BS
import codecs
import datetime as dt
import os

# Fecha de hoy
today = dt.date.today()
today = str(today)

directory = os.getcwd() + '/Pagina12_impresa_prueba_' + today
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
fp = codecs.open('Resumen' + today + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo, Seccion' + '\n')
fp.close()

suplementos = {'principal': '/principal.xml', u'Líbero': '/libero.xml', \
              u'No': '/no.xml', u'Espectáculos': '/espectaculos.xml', \
              u'Radar': '/radar.xml', u'Las12': '/las12.xml', \
              u'RadarLibros': '/libros.xml', u'Soy': '/soy.xml'}

for supl in suplementos.keys():

    # LLamado al RSS.
    pagina = 'http://www.pagina12.com.ar/diario/rss/' + suplementos[supl]
    feed = feedparser.parse(pagina)

    # Recorrido sobre las notas de la sección.
    for item in feed['entries']:

        # Título
        title = item['title']
        try:
            title = title.replace(u'\x93','"')
            title = title.replace(u'\x94','"')
            title = title.replace(u'\x96','-')
            title = title.replace(u'\x91', '\'')
            title = title.replace(u'\x92', '\'')
        except:
            pass

        # Sección
        if supl == 'principal':
            description = BS(item['description'], 'html.parser')
            section = description.find('em').getText()
        else:
            section = supl

        published_date = item['published_parsed']

        note_date = dt.date(published_date.tm_year, \
                    published_date.tm_mon, published_date.tm_mday)
        
        if note_date == dt.date.today():
            # Extracción de contenido            
            link = item['link']
            req = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req).read()
            soup = BS(html, 'html.parser')
            
            # Subtítulo
            try:
                subtitle = soup.find('p', {'class': 'intro'}).getText()
                subtitle = subtitle.replace('\n', '')
                subtitle = subtitle.replace(u'\x94', '"')
                subtitle = subtitle.replace(u'\x93', '"')
                subtitle = subtitle.replace(u'\x96', '-')
                subtitle = subtitle.replace(u'\x91', '\'')
                subtitle = subtitle.replace(u'\x92', '\'')
            except:
                subtitle = ''

            # Cuerpo
            try:
                body = soup.find(id = 'cuerpo').getText()
                body = body.replace(u'\x94', '"')
                body = body.replace(u'\x93', '"')
                body = body.replace(u'\x96', '-')
                body = body.replace(u'\x91', '\'')
                body = body.replace(u'\x92', '\'')
            except:
                body = ''

            # Guardado de la nota en formato: fecha, sección, título, subtítulo, contenido.
            fp = codecs.open('Nota' + str(id_nota) + '.txt', 'w', 'utf8')
            fp.write(today + '\n' + section + '\n' + title + '\n')
            fp.write(subtitle + '\n' + body + '\n')
            fp.close()
            
            # Guardado del titulo e id para rápida identificación.
            fp = codecs.open('Resumen' + today + '.txt', 'a', 'utf8')
            fp.write(str(id_nota) + '\t' + title + '\t' + section + '\n')
            fp.close()
             
            id_nota += 1         
