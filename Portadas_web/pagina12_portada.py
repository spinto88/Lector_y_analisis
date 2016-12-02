#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este programa guarda las noticias de la portada
de la web del diario Página 12 de las 18:00hs.
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

directory = os.getcwd() + '/Pagina12_portada_' + today
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

if True:

    # LLamado al RSS.
    pagina = 'http://www.pagina12.com.ar/diario/ultimas/index.html'
    req = Request(pagina, headers = {'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BS(html, 'html.parser')
    articles = soup.findAll('div', {'class':'ultimas_noticias'})

    for article in articles:

        # Título
        title = article.find('a').getText() 
        try:
            title = title.replace(u'\x93','"')
            title = title.replace(u'\x94','"')
            title = title.replace(u'\x91', '\'')
            title = title.replace(u'\x92', '\'')
            title = title.replace(u'\x96','-')
        except:
            pass
        try:
            link = 'http://www.pagina12.com.ar' + article.find('a')['href']
            req = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req).read()
            soup = BS(html, 'html.parser')
        except:
            continue

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
        fp.write(today + '\n' + title + '\n' + body + '\n')
        fp.close()
            
        # Guardado del titulo e id para rápida identificación.
        fp = codecs.open('Resumen' + today + '.txt', 'a', 'utf8')
        fp.write(str(id_nota) + '\t' + title + '\n')
        fp.close()
             
        id_nota += 1         
