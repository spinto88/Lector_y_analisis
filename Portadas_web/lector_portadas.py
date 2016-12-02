#!/usr/bin/python

import os
from datetime import date as dt

path = os.getcwd()

today = str(dt.today())

os.system('python ' + path + '/clarin_portada.py')
os.system('python ' + path + '/pagina12_portada.py')
os.system('python ' + path + '/herald_portada.py')

os.system('zip clarin_portada_' + today + '.zip Clarin_portada_' + today + '/*')
os.system('zip pagina12_portada_' + today + '.zip Pagina12_portada_' + today + '/*')
os.system('zip herald_portada_' + today + '.zip Herald_portada_' + today + '/*')
