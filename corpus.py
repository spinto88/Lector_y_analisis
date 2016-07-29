#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Definicion de clase Corpus, para consulta y 
uso de la base de datos .xml.
"""
from lxml import etree
from datetime import date
from nltk.tokenize import word_tokenize

class Note(object):

    def __init__(self, note):

        self.idNote = int(note.get('id'))

        self.title = note.find('title').text
        self.section = note.find('section').text
        self.subtitle = note.find('subtitle').text
        self.body = note.find('body').text

        self.day = int(note.find('date/day').text)
        self.month = int(note.find('date/month').text)
        self.year = int(note.find('date/year').text)

        self.date = date(self.year, self.month, self.day)

    def number_of_body_words(self):

        tokens = word_tokenize(self.body)
        return len(tokens)

class Corpus(object):

    def __init__(self, document):

        xmldoc = etree.parse(document)
        root = xmldoc.getroot()

        self.newspaper_name = root.find('name').text
        self.description = root.find('description').text
        self.notes = []
        for note in root.findall('note'):
            self.notes.append(Note(note))

