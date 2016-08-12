#!/usr/bin/python

import os
from datetime import date as dt

path = os.getcwd()

today = str(dt.today())

os.system('python ' + path + '/lanacion_impresa.py')
os.system('python ' + path + '/pagina12_impresa.py')
os.system('python ' + path + '/Tapas.py')

os.system('zip lanacion_impresa_' + today + '.zip LaNacion_impresa_' + today + '/*')
os.system('zip pagina12_impresa_' + today + '.zip Pagina12_impresa_' + today + '/*')
