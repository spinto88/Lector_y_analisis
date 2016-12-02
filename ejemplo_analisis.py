#!/usr/bin/env python
# -*- coding: utf-8 -*-
from corpus import Corpus
import datetime as dt
import matplotlib.pyplot as plt
import codecs

newspaper = Corpus('LaNacion.xml')

fp = codecs.open('Data_lsa.txt','a','utf-8')

counter = 0
for note in newspaper.notes:
    if (note.section == u'Política' and counter < 10) or (note.section == u'Deportes' and counter >= 10):
        fp.write(note.title + '\t' + note.body + '\n')
        counter += 1
        if counter == 20:
            break
fp.close()
    
"""

note = newspaper.getNoteById(0)
data = note.principal_words()

print data['body']
"""
#ewspaper.evolOfSectionPlot(u'Opinión')
