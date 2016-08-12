
from urllib2 import urlopen
import datetime as dt
import os 

today = dt.date.today()

mes = today.month
dia = today.day

string = ''
if mes < 10:
    string += '0' + str(mes) + '/'
else:
    string += str(mes) + '/'

if dia < 10:
    string += '0' + str(dia)
else:
    string += str(dia)

prensa = 'http://img.kiosko.net/2016/' + string + '/ar/ar_laprensa.750.jpg'
herald = 'http://img.kiosko.net/2016/' + string + '/ar/buenos_aires_herald.750.jpg'
pagina12 = 'http://img.kiosko.net/2016/' + string + '/ar/ar_pagina12.750.jpg'
clarin = 'http://img.kiosko.net/2016/' + string + '/ar/ar_clarin.750.jpg'
lanacion = 'http://img.kiosko.net/2016/' + string + '/ar/nacion.750.jpg'
larazon = 'http://img.kiosko.net/2016/' + string + '/ar/ar_razon.750.jpg'

nombres = ['Clarin', 'LaRazon', 'LaNacion', 'Pagina12', 'Herald', 'Prensa']
diarios = [clarin, larazon, lanacion, pagina12, herald, prensa]

ind_diario = 0

path = os.getcwd() + '/Tapas/' + str(dt.date.today())
try:
    os.mkdir(path)
except:
    pass

os.chdir(path)

for i in diarios:

   try:

       img = urlopen(i)

       localFile = open(nombres[ind_diario] + '.jpg', 'wb')

       localFile.write(img.read())

       localFile.close()

       ind_diario += 1

   except:
       pass

