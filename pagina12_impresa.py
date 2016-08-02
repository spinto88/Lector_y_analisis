#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa guarda las últimas noticias del RSS del diario Página 12,
tomadas a las 18:00 hs.
"""

import feedparser
from urllib2 import Request
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

id_nota = 0

# Guardado del titulo e id para rápida identificación.

fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
fp.write('#Id_nota, Titulo' + '\n')
fp.close()

if True:

    # LLamado al RSS.
    pagina = 'http://www.pagina12.com.ar/diario/rss/principal.xml'
    feed = feedparser.parse(pagina)

    # Recorrido sobre las notas de la sección.
    for item in feed['entries']:

        # Título, subtitulo, fecha.
        title = item['title']
        try:
            title = title.replace('u\x93','"')
            title = title.replace('u\x94','"')
            title = title.replace('u\x96','-')
            title = title.replace(u'\x91', '\'')
            title = title.replace(u'\x92', '\'')
        except:
            pass

        description = BS(item['description'], 'html.parser')
        date = item['published_parsed']
        date = dt.date(date.tm_year, date.tm_mon, date.tm_mday)

        section = description.find('em').getText()

        # Guarda la nota si es del día de hoy o del día de ayer.
        day_offset = dt.timedelta(days = 1)
        if date >= (today - day_offset):

            link = item['link']

            req = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req).read()
            soup = BS(html, 'html.parser')
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
            fp.write(str(date) + '\n' + section + '\n' + title + '\n')
            fp.write(subtitle + '\n' + body + '\n')
            fp.close()
            
            # Guardado del titulo e id para rápida identificación.
            fp = codecs.open('Resumen' + str(today) + '.txt', 'a', 'utf8')
            fp.write(str(id_nota) + '\t' + title + '\n')
            fp.close()
             
            id_nota += 1         
