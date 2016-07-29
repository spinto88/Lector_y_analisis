#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Definicion de clase Corpus, para consulta y 
uso de la base de datos .xml.
"""
from lxml import etree
from datetime import date
from datetime import timedelta
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

    def __eq__(self, other):

        if self.title == other.title \
        and self.body == other.body \
        and self.subtitle == other.subtitle \
        and self.section == other.section:
            return True
        else:
            return False

    def phraseInNote(self, phrase):

        phrase_lower = phrase.lower()
        phrase_upper = phrase.upper()
        phrase_capitalize = phrase.capitalize()

        phrases2check = [phrase, phrase_lower, \
                     phrase_upper, phrase_capitalize]

        for phrase2check in phrases2check:
            if phrase in self.title \
            or phrase in self.subtitle \
            or phrase in self.body:
                return True
            else:
                return False
        

    def numberOfBodyWords(self):

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

        self.deleteRepeatedNotes()
        

    def deleteRepeatedNotes(self):

        notes2remove = []
        
        for note in self.notes:
            for note2compare in self.notes:
                if note2compare == note and note2compare.date >= note.date \
                and note2compare.idNote != note.idNote:
                    notes2remove.append(note2compare.idNote)

        for idNote in notes2remove:
            for note in self.notes:
                if note.idNote == idNote:
                    self.notes.remove(note)
        

    def getNoteById(self, idNote):

        for note in self.notes:
            if note.idNote == idNote:
                return note       
        return 'id not found'
