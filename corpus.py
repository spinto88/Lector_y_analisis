#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Definicion de clase Corpus, para consulta y 
uso de la base de datos .xml.
"""

from xml.dom import minidom
from datetime import date

class Note(object):

    def __init__(self, note):

        self.idNote = int(note.getAttribute('id'))

        self.title = note.getElementsByTagName('title')[0].firstChild.data
        self.subtitle = note.getElementsByTagName('subtitle')[0].firstChild.data
        self.corpus = note.getElementsByTagName('corpus')[0].firstChild.data
        self.section = note.getElementsByTagName('section')[0].firstChild.data

        self.day = int(note.getElementsByTagName('day')[0].firstChild.data)
        self.month = int(note.getElementsByTagName('month')[0].firstChild.data)
        self.year = int(note.getElementsByTagName('year')[0].firstChild.data)

        self.date = date(self.year, self.month, self.day)
         

class Corpus(object):

    def __init__(self, document):
        self.db = minidom.parse(document)
        self.notes = []
        notes = self.db.getElementsByTagName('note')
        for note in notes:
            self.notes.append(Note(note))


    def getNoteById(self, idNote):

        for note in self.notes:
            if idNote == note.idNote:
                return note


        
"""
word = 'Macri'

doc = minidom.parse('LaNacion.xml')

notes = doc.getElementsByTagName('note')

data = {}
dates = []

for note in notes:

    month = int(note.getElementsByTagName('month')[0].firstChild.data)
    day = int(note.getElementsByTagName('day')[0].firstChild.data)

    title = note.getElementsByTagName('title')[0].firstChild.data
    corpus = note.getElementsByTagName('corpus')[0].firstChild.data
    if word in title or word in corpus:
        words = word_tokenize(title) + word_tokenize(corpus)
        try:
            data[str(current_date)] += words.count(word)
        except:
            data[str(current_date)] = words.count(word)

print data 
"""
