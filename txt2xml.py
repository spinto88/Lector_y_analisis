#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import date
from datetime import timedelta
import calendar

path = os.getcwd()

date_inicial = date(2016, 06, 15)
date_final = date.today()
day1 = timedelta(days = 1)

current_day = date_inicial

id_note = 0

fname = 'LaNacion.xml'

try:
    os.remove(fname)
except:
    pass

fp = open(fname, 'a')
fp.write('<?xml version="1.0" encoding="UTF-8"?>\n')
fp.write('<newspaper>\n') 
fp.write('\t<name>La Nacion</name>\n')
fp.write('\t<description>Notas del diario La Nacion del dia ' + str(date_inicial) + ' al ' + str(date_final) + '.</description>\n')
fp.write('\t<initial_date>\n')
fp.write('\t\t<day>' + str(date_inicial.day) + '</day>\n')
fp.write('\t\t<month>' + str(date_inicial.month) + '</month>\n')
fp.write('\t\t<year>' + str(date_inicial.year) + '</year>\n')
fp.write('\t</initial_date>\n')
fp.write('\t<final_date>\n')
fp.write('\t\t<day>' + str(date_final.day) + '</day>\n')
fp.write('\t\t<month>' + str(date_final.month) + '</month>\n')
fp.write('\t\t<year>' + str(date_final.year) + '</year>\n')
fp.write('\t</final_date>\n')
fp.close()

while current_day <= date_final:
   
  path_new = path + '/Notas' + str(current_day)

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
      fp = open(fname, 'a')
      fp.write('\t<note id="' + str(id_note) +'">\n')
      fp.write('\t\t<title>' + title + '</title>\n')
      fp.write('\t\t<section>' + section + '</section>\n')

      fp.write('\t\t<date>\n')
      fp.write('\t\t\t<day>' + str(current_day.day) + '</day>\n')
      fp.write('\t\t\t<month>' + str(current_day.month) + '</month>\n')
      fp.write('\t\t\t<year>' + str(current_day.year) + '</year>\n')
      fp.write('\t\t\t<day_of_the_week>' + \
      str(calendar.weekday(current_day.year, current_day.month, current_day.day)) + \
      '</day_of_the_week>\n')
      fp.write('\t\t</date>\n')

      fp.write('\t\t<subtitle>' + subtitle + '</subtitle>\n')
      fp.write('\t\t<body>' + body + '</body>\n')
      fp.write('\t</note>\n')
      fp.close()
      id_note += 1 

  current_day += day1

os.chdir(path)
fp = open(fname, 'a')
fp.write('</newspaper>\n') 
fp.close()

from shutil import copyfile
copyfile(fname, '/home/spinto/Escritorio/Lector_y_analisis/' + fname)
