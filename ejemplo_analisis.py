#!/usr/bin/env python
# -*- coding: utf-8 -*-
from corpus import Corpus
import datetime as dt
import matplotlib.pyplot as plt

newspaper = Corpus('LaNacion.xml')

note = newspaper.getNoteById(0)
data = note.principal_words()

print data['body']

#ewspaper.evolOfSectionPlot(u'Opinión')
