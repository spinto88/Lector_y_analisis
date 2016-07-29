#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import date
from datetime import timedelta

path = os.getcwd()

date_inicial = date(2016, 06, 15)
date_final = date(2016, 07, 28)
day1 = timedelta(days = 1)

current_day = date_inicial

id_note = 0

while current_day <= date_final:
   
  path_new = path + '/Notas' + str(current_day)

  fp = open('LaNacion.xml', 'a')
  fp.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  fp.write('<newspaper>\n') 
  fp.write('\t<name>La Nacion</name>\n')
  fp.write('\t<description>Notas del diario La Nacion del dia' + str(date_inicial) + ' al ' + str(date_final) + '.</description>\n')
  fp.close()

  for i in range(500):

      try:
        os.chdir(path_new)
        fp = open('Nota' + str(i) + '.txt', 'r')
        text = fp.read()
        fp.close()
      except:
        continue

      text = text.split('\n')
 
      section = text[0]    
      title = text[2].replace('&', '&amp;')
      subtitle = text[3].replace('&', '&amp;')

      body = text[4:]
      body = ''.join(body)
      body = body.replace('&', '&amp;')

      os.chdir(path)
      fp = open('LaNacion.xml', 'a')
      fp.write('\t<note id="' + str(id_note) +'">\n')
      fp.write('\t\t<title>' + title + '</title>\n')
      fp.write('\t\t<section>' + section + '</section>\n')

      fp.write('\t\t<date>\n')
      fp.write('\t\t\t<day>' + str(current_day.day) + '</day>\n')
      fp.write('\t\t\t<month>' + str(current_day.month) + '</month>\n')
      fp.write('\t\t\t<year>' + str(current_day.year) + '</year>\n')
      fp.write('\t\t</date>\n')

      fp.write('\t\t<subtitle>' + subtitle + '</subtitle>\n')
      fp.write('\t\t<body>' + body + '</body>\n')
      fp.write('\t</note>\n')
      fp.close()
      id_note += 1 

  current_day += day1

os.chdir(path)
fp = open('LaNacion.xml', 'a')
fp.write('</newspaper>\n') 
fp.close()

