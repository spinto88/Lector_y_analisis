#!/usr/bin/env python
# -*- coding: utf-8 -*-
from corpus import Corpus
import datetime as dt

newspaper = Corpus('LaNacion.xml')

palabra = u'brexit'

for note in newspaper.notes:
    if note.phraseInNote(palabra):
        print note.idNote, note.title, note.date
